"""
account_service.py

This module provides a class to manage user account operations such as:
- Creating user accounts
- Authenticating users
- Depositing and withdrawing funds
- Checking account balances
- Transferring money between accounts
- Displaying user information

Dependencies:
    - account_model.Account: For managing the system's user list.
    - user_model.User: For representing individual user accounts.
"""
import sqlite3
from datetime import datetime

class AccountService:
    """
    A class that provides various operations for managing user accounts 
    in an electronic wallet system.
    These operations include account creation, login authentication, 
    deposit, withdrawal, money transfer,and displaying user information.

    Methods:
        create_user_account(new_user): Creates a new user account in the database.
        check_account(current_user): Checks if a user account exists in the database.
        handle_login(current_user): Handles the login process by verifying the provided username and password.
        handle_deposit(current_user, deposit_value): Handles deposit transactions for a user account.
        check_enough_money(current_user, withdraw_value): Checks if the user has enough balance to withdraw.
        handle_withdraw(current_user, withdraw_value): Handles withdrawal transactions for a user account.
        handle_transfer(source_account, transfer_value, dest_username): Transfers money from one user to another.
        handle_user_info(current_user): Displays the user’s username and balance.
    """

    @classmethod
    def create_user_account(cls, new_user):
        """
        Creates a new user account in the database.

        Parameters:
            new_user (User): The user object containing username, password, and balance details.

        Returns:
            bool: True if the account was created successfully, False if the username already exists.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            if not cls.check_account(new_user.get_username()):
                sql = "Insert into Users (username, password, balance) values (?, ?, ?)"
                data = [new_user.get_username(), new_user.get_password(), new_user.get_balance()]
                connection.execute(sql, data)
                connection.commit()
                connection.close()
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def check_account(current_user):
        """
        Checks if a user account exists in the database.

        Parameters:
            current_user (User): The user object containing the username to check.

        Returns:
            bool: True if the account exists, False otherwise.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            sql = "SELECT username FROM Users WHERE username = ?"
            data = [current_user]
            row = connection.execute(sql, data).fetchone()
            connection.commit()
            connection.close()
            if row is None:
                return False
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def handle_login(current_user):
        """
        Verifies the login credentials by checking the username and password.

        Parameters:
            current_user (User): The user object containing the username and password to verify.

        Returns:
            bool: True if the username and password match, False otherwise.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            sql = "SELECT username, password FROM Users WHERE username = ? AND password = ?"
            data = [current_user.get_username(), current_user.get_password()]
            row = connection.execute(sql, data).fetchone()
            connection.commit()
            connection.close()
            if row is None:
                return False
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def handle_deposit(current_user, deposit_value):
        """
        Handles a deposit transaction for a user account.

        Parameters:
            current_user (User): The user object for whom the deposit will be made.
            deposit_value (float): The amount to deposit into the user’s account.

        Returns:
            bool: True if the deposit is successful, False if an error occurs.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            sql = "UPDATE Users SET balance = balance + ? WHERE username = ?"
            data = [deposit_value, current_user.get_username()]
            connection.execute(sql, data)
            
            now=str(datetime.now())
            hist_sql="Insert into Transactions (username,type,date,amount) values (?,?,?,?)"
            hist_data=[current_user.get_username(),"deposit",now,deposit_value]
            connection.execute(hist_sql,hist_data)
    
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    @staticmethod
    def check_enough_money(current_user, withdraw_value):
        """
        Checks if the user has enough balance to withdraw the requested amount.

        Parameters:
            current_user (User): The user object whose balance will be checked.
            withdraw_value (float): The amount to check against the user’s balance.

        Returns:
            bool: True if the user has enough balance, False otherwise.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            sql = "SELECT balance FROM Users WHERE username = ?"
            data = [current_user.get_username()]
            balance_value = connection.execute(sql, data).fetchone()[0]
            connection.commit()
            connection.close()
            return balance_value >= withdraw_value
        except Exception as e:
            print(f"Error: {e}")
            return False

    @classmethod
    def handle_withdraw(cls, current_user, withdraw_value,comming_from="w"):
        """
        Handles a withdrawal transaction for a user account.

        Parameters:
            current_user (User): The user object for whom the withdrawal will be made.
            withdraw_value (float): The amount to withdraw from the user’s account.

        Returns:
            bool: True if the withdrawal is successful, False if an error occurs or if the user doesn't have enough money.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            if cls.check_enough_money(current_user, withdraw_value):
                sql = "UPDATE Users SET balance = balance - ? WHERE username = ?"
                data = [withdraw_value, current_user.get_username()]
                connection.execute(sql, data)
                
                #in order to not save a withdraw operation during the transfer
                if comming_from=="w":
                    now=str(datetime.now())
                    hist_sql="Insert into Transactions (username,type,date,amount) values (?,?,?,?)"
                    hist_data=[current_user.get_username(),"withdraw",now,withdraw_value]
                    connection.execute(hist_sql,hist_data)
                
                connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()
    #transfer feha moshkla en baro7 anfz withdraw fa by7sal tanfez lel foo2 dih fa battsgl fel db.
    #momken a7ot argument foo2 ya3deny mel kalam dah en law ana gay mel transfer sa3tha manfzsh el insertion transaction.
    @classmethod
    def handle_transfer(cls, source_account, transfer_value, dest_username):
        """
        Handles a money transfer between two user accounts.

        Parameters:
            source_account (User): The user object from whose account the money will be withdrawn.
            transfer_value (float): The amount to transfer.
            dest_username (str): The username of the recipient user account.

        Returns:
            bool: True if the transfer is successful, False if there’s an error or if the user doesn't have enough money.
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            if not cls.check_account(dest_username):
                print("There is no account with this username.")
                return False
            if not cls.handle_withdraw(source_account, transfer_value,"t"):
                print("Not enough money to transfer.")
                return False
            
            sql = "UPDATE Users SET balance = balance + ? WHERE username = ?"
            data = [transfer_value, dest_username]
            connection.execute(sql, data)
            
            now=str(datetime.now())
            hist_sql="Insert into Transactions (username,type,related_username,date,amount) values (?,?,?,?,?)"
            hist_data=[source_account.get_username(),"transfer",dest_username,now,transfer_value]
            connection.execute(hist_sql,hist_data)
            
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    @staticmethod
    def handle_user_info(current_user):
        """
        Displays the user’s username and balance.

        Parameters:
            current_user (User): The user object whose information will be displayed.

        Returns:
            None
        """
        try:
            connection = sqlite3.connect("EWallet.db")
            sql = "SELECT username, balance FROM Users WHERE username = ?"
            data = [current_user.get_username()]
            row = connection.execute(sql, data).fetchone()
            connection.commit()
            connection.close()
            print(f"{row[0]} {row[1]}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def handle_user_history(current_user):
        try:
            connection=sqlite3.connect("EWallet.db")
            sql="Select * from Transactions where username=?"
            data=[current_user.get_username()]
            rows=connection.execute(sql,data).fetchall()
            connection.commit()
            connection.close()
            for row in rows:
                for elem in row[1:]:
                    if elem is not None:
                        print(elem,end=" ")
                print()
        except Exception as e:
            print(f"Error: {e}")
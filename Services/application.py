"""
main.py

This module contains the main logic of the application, which allows users to signup, login, and perform various operations 
such as deposit, withdraw, transfer money, and view their account information. The logic is divided into different methods 
for each functionality and validates user inputs using the `Validate` class from the `Services.validation` module.
"""

from Services.account_service import AccountService
from Model.user_model import User
from Services.validation import Validate

class Main:
    """
    The Main class is responsible for managing the user interface and flow of the application. It facilitates user actions 
    such as signing up, logging in, depositing money, withdrawing money, transferring money, and viewing account information. 
    All user actions are validated and processed using services from AccountService.
    """

    @classmethod
    def start(cls):
        """
        Starts the main application and displays the initial options to the user (Signup, Login, Exit).
        Handles incorrect user input and exits the program after 4 invalid attempts.

        Args:
            None

        Returns:
            None
        """
        error_choice_counter = 0
        print("------------------Hello Sir------------------------")
        while True:
            print("1.Signup 2.Login 3.Exit ")
            value = input("Enter your choice:")
            if value == '1':
                cls.signup()
            elif value == '2':
                cls.login()
            elif value == '3':
                return
            else:
                error_choice_counter += 1
                if error_choice_counter != 4:
                    print("Please Enter valid Choice")
            if error_choice_counter == 4:
                return

    @staticmethod
    def extract_account(page):
        """
        Extracts and validates the account information (username and password) based on the page type (signup or login).
        
        Args:
            page (str): The page type ("signup" or "login") that determines the validation rules.

        Returns:
            user (User or None): Returns a User object if the data is valid; otherwise, returns None.
        """
        username = input("please enter your username:")
        if Validate.validate_username(username) is False and page == "signup":
            print("you entered invalid username; length must be greater than 2 and starts with uppercase")
            return None
        password = input("please enter your password:")
        if Validate.validate_password(password) is False and page == "signup":
            print("you entered invalid password; length must be greater than 5 and contains uppercase and lowercase and special char and number")
            return None
        user = User(username, password)
        return user

    @classmethod
    def signup(cls):
        """
        Handles the user signup process. Prompts the user to enter their username and password, validates them, 
        and creates the user account. If the username is already taken, it displays an error message.
        
        Args:
            None

        Returns:
            None
        """
        print("------------------Hello From Signup Page------------------------")
        user = cls.extract_account("signup")
        if user is None:
            return 
        account_created = AccountService.create_user_account(user)
        if account_created:
            cls.login()
        else:
            print("this username is already registered")
            return

    @classmethod
    def login(cls):
        """
        Handles the user login process. Prompts the user to enter their username and password, validates them, 
        and checks if the account exists. If successful, it redirects to the menu page.
        
        Args:
            None

        Returns:
            None
        """
        print("------------------Hello From Login Page------------------------")
        user = cls.extract_account("login")
        account_found = AccountService.handle_login(user)
        if account_found:
            cls.menu_page(user)
        else:
            print("you entered wrong username or password")
            

    @classmethod    
    def menu_page(cls, user):
        """
        Displays the menu page after a successful login. 
        The user can choose between deposit, withdraw, transfer, 
        show account details, or exit. 
        Invalid choices prompt the user to enter a valid option.

        Args:
            user (User):The logged-in user whose actions are being handled.

        Returns:
            None
        """
        error_choice_counter = 0
        print("------------------Hello From Menu Page------------------------")
        while True:
            print("1.Deposit 2.Withdraw 3.Transfer 4.Show 5.History 6.Exit")
            value = input("Enter your choice:")
            if value == '1':
                cls.deposit(user)
            elif value == '2':
                cls.withdraw(user)
            elif value == '3':
                cls.transfer_money(user)
            elif value == '4':
                cls.show_user(user)
            elif value=='5':
                cls.history_page(user)
            elif value == '6':
                return
            else:
                error_choice_counter += 1
                if error_choice_counter != 4:
                    print("Please Enter valid Choice")
            if error_choice_counter == 4:
                return

    @staticmethod
    def deposit(user):
        """
        Handles the deposit operation. Prompts the user to enter the deposit amount, performs the deposit, 
        and shows the result of the operation.

        Args:
            user (User): The logged-in user who is making the deposit.

        Returns:
            None
        """
        print("------------------Hello From Deposit Page------------------------")
        deposit_value = float(input("Please Enter the amount you need to deposit:"))
        deposit_trans = AccountService.handle_deposit(user, deposit_value)
        if deposit_trans:
            print("YOUR DEPOSIT OPERATION PERFORMED SUCCESSFULLY")
        else:
            print("THERE IS SOMETHING WRONG! PLEASE TRY AGAIN LATER")

    @staticmethod
    def withdraw(user):
        """
        Handles the withdraw operation. Prompts the user to enter the withdrawal amount, performs the withdrawal, 
        and shows the result of the operation.

        Args:
            user (User): The logged-in user who is making the withdrawal.

        Returns:
            None
        """
        print("------------------Hello From Withdraw Page------------------------")
        withdraw_value = float(input("Please enter amount you need to withdraw:"))
        withdraw_trans = AccountService.handle_withdraw(user, withdraw_value)
        if withdraw_trans:
            print("YOUR WITHDRAW OPERATION PERFORMED SUCCESSFULLY")
        else:
            print("NO ENOUGH MONEY TO WITHDRAW THIS VALUE")

    @staticmethod
    def show_user(user):
        """
        Displays the user's account information, including their username and balance.

        Args:
            user (User): The logged-in user whose information is being displayed.

        Returns:
            None
        """
        print("------------------Hello From Info Page------------------------")
        AccountService.handle_user_info(user)

    @staticmethod
    def transfer_money(user):
        """
        Handles the money transfer operation. Prompts the user to enter the destination account username and transfer amount, 
        performs the transfer, and shows the result of the operation.

        Args:
            user (User): The logged-in user who is making the transfer.

        Returns:
            None
        """
        print("------------------Hello From Transfer Page------------------------")
        account = input("Enter the username of the account you need to transfer to:")
        money = float(input("Enter the amount you need to transfer:"))
        transfer_operation = AccountService.handle_transfer(user, money, account)
        if transfer_operation:
            print("YOUR Transfer OPERATION PERFORMED SUCCESSFULLY")
        else:
            print("PLEASE TRY AGAIN LATER!")
    @staticmethod
    def history_page(user):
        AccountService.handle_user_history(user)
"""
user_module.py

This module defines the User class, which represents a system user with private
attributes for username, password, and account balance. It provides controlled
access to these attributes through getter and setter methods.

Example:
    user1 = User("alice", "securepassword123")
    user1.set_balance(100.0)
    print(user1.get_username())  # Output: alice
    print(user1.get_balance())   # Output: 100.0
"""

class User:
    """
    A class to represent a user with a username, password, and account balance.

    Attributes:
        __username (str): The user's username (private).
        __password (str): The user's password (private).
        __balance (float): The user's account balance (private, default is 0).
    """

    def __init__(self, username, password):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.__username = username
        self.__password = password
        self.__balance = 0

    def set_username(self, username):
        """
        Sets the username for the user.

        Args:
            username (str): The new username to set.
        """
        self.__username = username

    def set_password(self, password):
        """
        Sets the password for the user.

        Args:
            password (str): The new password to set.
        """
        self.__password = password

    def set_balance(self, balance):
        """
        Sets the account balance for the user.

        Args:
            balance (float): The balance amount to set.
        """
        self.__balance = balance

    def get_username(self):
        """
        Returns the user's username.

        Returns:
            str: The current username.
        """
        return self.__username

    def get_password(self):
        """
        Returns the user's password.

        Returns:
            str: The current password.
        """
        return self.__password

    def get_balance(self):
        """
        Returns the user's account balance.

        Returns:
            float: The current balance.
        """
        return self.__balance

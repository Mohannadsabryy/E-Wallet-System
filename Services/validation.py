"""
validate.py

This module provides static methods for validating user input, including usernames and passwords.
It uses helper methods from the string_helper module for password strength checks.
"""

from Services.string_helper import Helper

class Validate:
    """
    A utility class for validating user input such as usernames and passwords.
    All methods are static since they do not depend on any instance or class-level state.
    """

    @staticmethod
    def validate_username(username):
        """
        Validates a username based on the following criteria:
        - Must be at least 3 characters long
        - Must start with an uppercase letter (A-Z)

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if the username is valid, False otherwise.
        """
        if len(username) >= 3 and 'A' <= username[0] <= 'Z':
            return True
        return False

    @staticmethod
    def validate_password(password):
        """
        Validates a password based on the following criteria:
        - Must be at least 6 characters long
        - Must contain at least one lowercase letter
        - Must contain at least one uppercase letter
        - Must contain at least one numeric digit
        - Must contain at least one special character ($, @, &, -)

        This method uses the Helper class from string_helper to perform these checks.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password meets all criteria, False otherwise.
        """
        if (
            len(password) >= 6 and
            Helper.contain_lower_case(password) and
            Helper.contain_upper_case(password) and
            Helper.contain_number(password) and
            Helper.contain_special(password)
        ):
            return True
        return False

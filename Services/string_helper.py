"""
helper.py

This module provides static utility methods for analyzing strings,
such as checking for uppercase letters, lowercase letters, digits, and special characters.
"""

class Helper:
    """
    A utility class that provides methods to check character contents in a string.
    All methods are static since they do not depend on class or instance state.
    """

    @staticmethod
    def contain_upper_case(text):
        """
        Checks if the string contains at least one uppercase letter.

        Args:
            text (str): The string to check.

        Returns:
            bool: True if at least one uppercase letter is found, False otherwise.
        """
        for ch in text:
            if 'A' <= ch <= 'Z':
                return True
        return False

    @staticmethod
    def contain_lower_case(text):
        """
        Checks if the string contains at least one lowercase letter.

        Args:
            text (str): The string to check.

        Returns:
            bool: True if at least one lowercase letter is found, False otherwise.
        """
        for ch in text:
            if 'a' <= ch <= 'z':
                return True
        return False

    @staticmethod
    def contain_special(text):
        """
        Checks if the string contains at least one special character ($, @, &, -).

        Args:
            text (str): The string to check.

        Returns:
            bool: True if at least one special character is found, False otherwise.
        """
        for ch in text:
            #set lookup time is o(1) but list is o(n) so here it is better to use set.
            if ch in {'$', '@', '&', '-'}:
                return True
        return False

    @staticmethod
    def contain_number(text):
        """
        Checks if the string contains at least one numeric digit.

        Args:
            text (str): The string to check.

        Returns:
            bool: True if at least one digit is found, False otherwise.
        """
        for ch in text:
            if '0' <= ch <= '9':
                return True
        return False

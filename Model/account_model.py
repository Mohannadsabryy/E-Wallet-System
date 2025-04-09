"""
account_model.py

This module contains the `Account` class, which represents the wallet and provides methods related to the wallet's
name.

Attributes:
    - __wallet_name (str): A class-level attribute representing the name of the wallet. This is a constant value 
      and is set to "InstaPay" by default.

Methods:
    - get_wallet_name(cls): A class method that returns the name of the wallet.
    
Usage:
    - The `Account` class provides access to the wallet's name through the `get_wallet_name()` method, which can 
      be used to retrieve the wallet name in other parts of the application.

Example:
    # To get the wallet name
    wallet_name = Account.get_wallet_name()
    print(wallet_name)  # Output: "InstaPay"
"""

class Account:
    # Class-level attribute to hold the wallet's name
    __wallet_name = "InstaPay"
    
    @classmethod
    def get_wallet_name(cls):
        """
        A class method to retrieve the name of the wallet.

        Returns:
            str: The name of the wallet, which is "InstaPay".
        """
        return cls.__wallet_name

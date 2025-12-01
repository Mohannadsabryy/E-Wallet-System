"""
main.py

This script is the entry point for the INSTAPAY application. It sets up the terminal output, displaying a stylized 
"INSTAPAY" logo using the pyfiglet library and prints it in yellow using the termcolor library. After displaying the logo, 
it invokes the `start` method from the `Main` class in the `Services.application` module to begin the application's operation.

Dependencies:
    - termcolor: For coloring terminal text.
    - pyfiglet: For generating ASCII art of the text "INSTAPAY".
    - Services.application.Main: The module and class that contains the logic to start the application.

Execution Flow:
    1. The script starts by importing the required libraries and modules.
    2. It generates an ASCII art of the text "INSTAPAY" using pyfiglet and colors it yellow using termcolor.
    3. It calls `Main.start()` to initiate the application's main functionality.

Usage:
    This script is intended to be run from the command line. It will display the ASCII art "INSTAPAY" logo and 
    then start the application by invoking the `start` method in the `Main` class.

Example:
    python main.py
"""

from Services.application import Main
import termcolor
import pyfiglet


if __name__ == "__main__":
    print("hello from my Mbranch")
    # Start the application
    Main.start()

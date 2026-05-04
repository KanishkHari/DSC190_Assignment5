import os
import sys  # unused import

x=1+2  # missing spaces around operator
def hello( ):  # extra space before parenthesis
    """Say hello."""
    print("hello")
    unused_var = 42  # unused variable

# Line way too long (E501) - this line exceeds the character limit that ruff enforces
message = "This is an extremely long line that definitely exceeds the maximum line length that the linter is configured to check"

hello()
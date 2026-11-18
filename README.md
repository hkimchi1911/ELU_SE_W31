Shopping Cart

Codebase:

This project is a Python program that calculates and displays the total price of items in a shopping cart.
The original codebase contained several issues related to code quality, potential bugs, and coding standards. The code has been improved to make it more readable and reliable.

Tasks

GitHub Actions Setup:
A GitHub Actions workflow has been created in .github/workflows/ci.yml to automate code checking and testing.

Automated Static Analysis:
The project uses flake8 to check the shopping_cart.py script and test file for coding style issues.
The static analysis runs automatically whenever changes are pushed to the repository.

Automated Testing:
The project uses Python's built-in unittest framework to test the shopping_cart.py script.
The test suite checks the total price calculation and handles an empty shopping cart.
GitHub Actions automatically runs the tests whenever changes are pushed.

Workflow Integration:
The GitHub Actions workflow includes two steps:
•	Run flake8 for static analysis.
•	Run unittest for automated testing.
Both checks must pass for the workflow to complete successfully.

# snbank

This project was to create a basic banking system that stores data using the Python File System. 

1. The program reads the staff.txt file and allows a pre-registered user to login if the username and password supplied at the login console is a match. The user is allowed an infinite number of attempts to input the correct login information.

2. The user session is tracked by creating a session.txt file after a successful user login which is deleted when the user logs out.

3. A logged in user can choose to either create a new bank account, check existing account details or logout.

4. Creating bank account saves the user's account name, opening balance, account type and account email. It also generates a unique 10 digit account number.

5. To check existing account details, the program returns all saved account details related to an account number query.

6. The Close App feature terminates the program.

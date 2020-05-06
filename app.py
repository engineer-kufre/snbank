import random
import os
import os.path

login = False

# function to check if user exists
def check_login(login):
    
    username = input('Please enter your username: ').lower()
    password = input('Please enter your password: ').lower()
    staff = open('staff.txt', 'r')
    listOfStaff = []
    dictionary = {}
    for line in staff:
        line = line.strip()
        if line == '':
            listOfStaff.append(dictionary)
            dictionary = {}
        else:
            pair = line.split(' ')
            if len(pair) == 2:
                key, value = pair
                dictionary[key] = value
            else:
                key = pair[0]
                value = pair[1] + ' ' + pair[2]
                dictionary[key] = value
    listOfStaff.append(dictionary)
    
    for staff in listOfStaff:
        if username == staff['username'] and password == staff['password'] :
            print("Login Successful!")
            login = True
            # create session file
            session = open('session.txt', 'w')
            session.write(staff['full_name'])
            
    if login == False:
        print('Wrong username or password! Try again')
    return login

# master function for all operations
def operations(login):
    choice = input(
'''What would you like to do?
Please select an option using the number assigned:
1 : Create new bank account
2 : Check Account Details
3 : Logout
''')
    # create new account
    if int(choice) == 1:
        account_name = input('Enter account name: ')
        opening_balance = input('Enter opening balance: ')
        account_type = input('Enter account type(Current OR Savings): ')
        account_email = input('Enter account email: ')
        account_number = ''
        for i in range(10):
            account_number += str(random.randint(0, 9))
        account_number = int(account_number)
        print(f'Your new account_number is {account_number}')
        
        customer = open('customer.txt', 'a')
        customer.writelines(
f'''account_name {account_name}
opening_balance {opening_balance}
account_type {account_type}
account_email {account_email}
account_number {account_number}
''')
        customer.close()
    
    # check account details
    elif int(choice) == 2:
        account_number = input('To check your account details, please enter your account number: ')
        customer = open('customer.txt', 'r')
        dictionary = {}
        for line in customer:
            line = line.strip()
            
            pair = line.split(' ')
            if len(pair) == 2:
                key, value = pair
                dictionary[key] = value
            else:
                key = pair[0]
                value = pair[1] + ' ' + pair[2]
                dictionary[key] = value
        if dictionary['account_number'] == account_number:
            print('Here are your account details:')
            print('')
            for key in dictionary:
                print(f'{key}: {dictionary[key]}')
        else:
            print('Sorry this account does not exist. Please try again.')
    
    # logout and delete session
    elif int(choice) == 3:
        os.remove('session.txt')
        login = False
    return login


close_app = False 

# check if app is closed or open
while close_app == False:
    # check if app was closed while user was still logged in
    message = ''
    try:
        session = open('session.txt', 'r')
    except IOError:
        message = 'Session file does not exist'
    else:
        session.close()
        
    if message != '':
        option = input('''
Select an option by entering the corresponding number:
1 : Staff Login
2 : Close App
''')
    else:
        login = True
        option = 1
        
    # staff login attempt(successful or not)
    if int(option) == 1:
        while login == False:
            login = check_login(login)
        
        # login successful
        while login == True:
            session = open('session.txt', 'r')
            name = session.read()
            session.close()
            print(f'Welcome {name}!')
            login = operations(login)
            
    # close app
    elif int(option) == 2:
        close_app = True



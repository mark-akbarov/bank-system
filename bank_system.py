acc_list=['John', 'Doe', 'Mama']
pin_list = [1234, 5678, 1231]


class Bank:

    def __init__(self):
        self.balance = 0

    def menu(self):
        print('''
            1. Create Account
            2. Login 
            3. Exit
        ''')
        user_input = int(input('Enter Command: '))
        if user_input == 1:
            Account().create()
        elif user_input == 2:
            Account().login()
        elif user_input == 3:
            exit()
        else:
            print('Invalid Input')

    def login_menu(self):
        print('''
            1. Deposit money
            2. Withdraw money 
            3. Logout
        ''')
        user_input = int(input('Enter Command: '))
        if user_input == 1:
            Bank().deposit()
        elif user_input == 2:
            Bank().withdraw()
        elif user_input == 3:
            Bank().menu()
        else:
            print('Invalid Input')

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)
        Bank().login_menu()
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance  ")
        Bank().login_menu()


class Account:
    def login(self):
        name_input = input('Enter you name: ')
        pin_input = int(input('Enter your pin: '))
        i = -1
        while i < len(acc_list) - 1:
            i += 1
            if name_input == acc_list[i]:
                if pin_input == pin_list[i]:
                    print(f'Welcome back {name_input}')
                    return Bank().login_menu()
                else:
                    print('Your username and password did not match')
                    Account.login()
        return Bank().menu()
        

    def create(self):
        name = input('\nEnter your name: ')
        while True:
            try:
                pin = int(input('\nEnter desired pin(Only numbers allowed): '))
                break
            except:
                print('Your pin should NOT involve any characters')
        if pin>9999:
                print('Error! Only four numbers are allowed')
                return Account().create()
        acc_list.append(name)
        pin_list.append(pin)
        print(f'Hello {name}, your account has been created\n')
        Bank().menu()


Bank().menu()



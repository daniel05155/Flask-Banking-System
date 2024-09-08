import json
import re
import subprocess as sp
from time import sleep, time


def system_about():
    print('''==========ABOUT US==========
          This project has been created by SungTe Hsu.\n''')

def developer_mode(user_data):
    print(f'{user_data}\n')
    sleep(5)

def clear():
    tmp = sp.call('cls', shell=True)

def validate_name(name):
    pattern = r'^[A-Za-z ]+$'      
    return bool(re.match(pattern, name))

# --- Sign up --- #
def sign_up(user_data, path_json):
    clear()
    new_info={}

    # Name #
    print(f'Enter your personal information:\n')
    name_checker=True
    while name_checker:
        first_name=input('First Name:')
        last_name=input('Last Name:')
        full_name = first_name + ' ' + last_name
        if validate_name(full_name):
            new_info['Name']=full_name
            name_checker=False
        else:
            print("Invalid Input!! Enter Your Name Again: \n")

        # for i in range(len(full_name)):
        #     cha_num = ord(full_name[i])
        #     if cha_num==32 or (cha_num>=65 and cha_num<=90) or (cha_num>=97 and cha_num<=122):
        #         new_info['name']=full_name 
        #         name_check=False
        #     else:
        #         name_check=True
        #         print('Please enter a valid name.')
        #         break
    print(f"Welcome {full_name} to the Bank of XYZ\n")

    # Password (PIN) #
    PIN_checker=True
    while PIN_checker:
        PIN_enter = input("Enter your 6-digit PIN: ")
        PIN_enter_check = input("Re-enter your 6-digit PIN: ")
        if PIN_enter==PIN_enter_check:
            if len(PIN_enter)==6:
                new_info['PIN']=PIN_enter
                PIN_checker=False
            else:
                PIN_checker=True
                print("Invalid Input!! Enter Your PIN Again: \n")
        else:
            PIN_checker=True
            print("PIN does not match our rule. Please Enter Again.\n")

    if PIN_checker==False:
        new_info['PIN'] = PIN_enter
        print("PIN is set successfully.\n")

    # Set Account Number #
    new_info['AccNumber'] = len(user_data['Users'])+1
    print(f"Your Account Number is: {new_info['AccNumber']}")

    # Set Account Balance (Default:0) #
    new_info['Balance'] = 0
    print(f"Your Account Balance is: {new_info['Balance']}")
    sleep(2)

    # Save the new user information #
    user_data['Users'].append(new_info)
    with open(path_json, 'w') as file:
        json.dump(user_data, file, indent=2)
        # json.dump(user_data, file)

    print(f"Already saved information of new customer named {full_name}\n")


# --- Existing User --- #
def Existing_User(user_data, path_json):
   
    # --- Log in --- #
    user_checker = True
    while user_checker:
        account_num = int(input('Please enter your account number:'))
        if account_num<=len(user_data['Users']) and account_num>0:
            username = input('Please enter the username:')
            password = input('Please enter the PIN (Password):')

            if username == user_data['Users'][account_num-1]['Name'] and password == user_data['Users'][account_num-1]['PIN']:
                print(f'{"="*10}Log in successfully.{"="*10}')
                user_checker=False
            else:
                print('Invalid username or passowrd !!!')
                sleep(2)
        else:
            print(f'{"="*5} Invalid Account Number !!! {"="*5}')
            sleep(2)

    # Account Details #
    user_number = account_num-1     
    login_user = user_data['Users'][user_number]

    # --- Bank Operations --- #
    work_status = True
    while work_status:
        choice = int(input('Please enter the service items: 1.Deposit, 2.Withdraw, 3.Transfer, 4.Balance Check, 5.Log out\n'))
        
        # --- Deposit --- #
        if choice==1:
           amount = int(input('Please enter the DEPOSIT amount:'))
           if amount>0:
                login_user['Balance'] += amount
                with open(path_json, 'w') as file:
                    json.dump(user_data, file, indent=2)
           else:
               print(f'{"="*5} Invalid Deposit !!! {"="*5}')

        # --- Withdraw --- #
        elif choice==2:
            amount = int(input('Please enter the WITHDRAW amount:'))
            if amount>0 and amount <= login_user['Balance']:
                login_user['Balance'] -= amount
                with open(path_json, 'w') as file:
                    json.dump(user_data, file, indent=2)
            else:
                print(f'{"="*5} Invalid Withdraw !!! {"="*5}')

        # --- Transfer --- #
        elif choice==3:
            acc_num_transfer = int(input('Please enter the number of transfered account:'))
            idx_acc_transfer = acc_num_transfer-1

            if idx_acc_transfer>=0 and idx_acc_transfer<len(user_data['Users']):
                transfered_user = user_data['Users'][idx_acc_transfer]
                money_transfer = int(input('Please enter the account number you want to transfer:'))

                # Check the balance of log-in user
                if money_transfer > 0 and money_transfer <= login_user['Balance']:
                    transfered_user['Balance'] += money_transfer
                    login_user['Balance'] -= money_transfer
                    # print(f'transfered-user Balance{}')
                    tmp=login_user['Balance']
                    print(f'Login-user Balance{tmp}')

                    with open(path_json, 'w') as file:
                        json.dump(user_data, file, indent=2)
                else:
                    print('INSUFFICIENT Transfer Amount !!!')
            else:
                print('Invalid transfered account number !!!')
        
        # --- Balance Checking --- #
        elif choice==4:
            print(f'Your current balance is: {user_data["Users"][user_number]["Balance"]}')

        # --- Log out --- #
        else:
            work_status=False
            print(f'{"="*5}Log out successfully.{"="*5}')

# Main Menu
def main():
    
    path_json = './customer_account.json'
    with open(path_json, 'r') as file:
        user_data=json.load(file)

    while True:
        print(f'{"="*20} Welcome to the Bank {"="*20}')
        service = int(input('Please enter the service items: 1.Sign up, 2.Log in, 3.Developed Mode, 4.About\n'))  # Lack exit function
        
        if service==1:
            clear()
            sign_up(user_data, path_json)

        elif service==2:
            clear()
            Existing_User(user_data, path_json)
        
        elif service==3:
            developer_mode(user_data)

        elif service==4:
            system_about()

        else:
            print('Invalid Input!!! Please enter the correct service.\n')
            sleep(2)
            clear()
        
if __name__ =='__main__':
    main()
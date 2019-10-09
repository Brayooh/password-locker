#!/usr/bin/env python3.6

import random
from locker import Credential, User


def create_user_account(user_name, pass_word):
    """
    Function to create a new account
    """
    new_user = User(user_name, pass_word)
    return new_user


def save_user_account(user):
    """
    Function to save user account
    """
    user.save_user()


def check_existing_users(characters):
    """
    Function that checks if a user exists with those characters and return a boolean
    """
    return User.user_exist(characters)


def create_credentials(view_password, account, login_name, pass_word):
    """
    Function to create a new credential
    """
    new_credential = Credential(view_password, account, login_name, pass_word)
    return new_credential


def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.del_credential()


def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that acc_name and return a Boolean
    '''
    return Credential.credential_exist(account)


def find_credential(account):
    '''
    Function that finds a credential by acc_name and returns the credential
    '''
    return Credential.find_by_account(account)


def display_credentials():
    """
    Function that returns the credentials list
    """
    return Credential.display_credentials()


def main():
    print("Hello! Welcome to the Password Locker. What is your name?")
    u_name = input('Enter a choice: ').lower().strip()
    print("\n")
    print(f"Hello {u_name}!! What would you like to do?")
    print("-" * 30)
    while True:
        print("\nUse these short codes below:")
        print('')
        print("\n ca - create an account \n li - login \n ex - exit password locker")
        short_code = input('Enter a choice: ').lower().strip()
        print("-" * 20)

        if short_code == 'ca':

            print("\nEnter a desired user name;")
            print('')
            user_name = input('Enter a choice: ').lower().strip()
            print("-" * 20)

            print("\nEnter a desired password;")
            print('')
            pass_word = input('Enter a choice: ').lower().strip()
            print("-" * 30)
            # create and save new account.
            save_user_account(create_user_account(user_name, pass_word))

            print("\n")
            print(f"New Account created.\n")

        elif short_code == "li":
            print("\nLogin to your account")
            print("-"*20)
            print("\nUsername?")
            user_name = input('Enter a choice: ').lower().strip()
            print("\nPassword?")
            print("-"*10)
            user_password_input = input('Enter a choice: ').lower().strip()
            view_password = user_password_input
            if check_existing_users(user_password_input):
                print("\n Welcome!")
                print("-" * 10)
                print('')
                print(
                    'Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n  \n ex-Exit')

                short_code = input('Enter a choice: ').lower().strip()
                print("-" * 60)
                if short_code == 'ex':
                    print(" ")
                    print(f'Goodbye {user_name}')
                    break
                elif short_code == 'cc':
                    print(' ')
                print("\n Enter your account(twitter, facebook, linkedIn).")
                print('')
                account = input('Enter a choice: ').lower().strip()
                print("-"*40)

                print(f"\n Enter your {account} account login name.")
                print('')
                login_name = input('Enter a choice: ').lower().strip()
                print("-"*45)

                print("\n Choose:")
                print('')
                print(
                    "'gp' - generate a password using password-locker \n'cp' - create your own password")
                password_creation_input = input('Enter a choice: ').lower().strip()
                print("-"*10)
                if password_creation_input == "cp":
                    print("\nEnter your password")
                    print('')
                    pass_word = input('Enter a choice: ').lower().strip()
                    print("-"*10)
                elif password_creation_input == "gp":
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    pass_word = "".join(random.choice(chars) for _ in range(8))
                    print(f"\nYour password is: **{pass_word}**")
                    print("-"*20)

                save_credentials(create_credentials(
                    view_password, account, login_name, pass_word))
                print("\n")
                print(
                    f"New credentials **{account}**, **{login_name}**, **{pass_word}** created")
                print("-" * 30)

            else:
                print("Wrong password or username. Please Try again.\n Username?")
                print("-"*20)
                user_name = input('Enter a choice: ').lower().strip()
                print("\nPassword?")
                print("-"*20)
                pass_word = input('Enter a choice: ').lower().strip()
                if check_existing_users(user_password_input):
                    print("\nWelcome back!")
                else:
                    print("You don't have an account.\n")

            while True:
                print( 
                        'Navigation codes: \n cc-Create a Credential \n dc-Display Credentials\n rc-delete credential \n ex-Exit')

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of your credentials:")
                print("-"*40)

                for credential in display_credentials():
                    print(
                        f"\nAccount: {credential.account}\nLogin Name: {credential.login}\nAccount Password: {credential.password}")
            else:
                print("\n You don't seem to have any credentials saved yet")

        elif short_code == 'rc':
            print("Enter the account name you want to delete")

            del_account = input('Enter a choice: ').lower().strip()
            if check_existing_credentials(del_account):
                del_credential(find_credential(del_account))

                print(f"Deleted credentials of {del_account}")
                print("-" * 30)

            else:
                print("That credential does not exist")

        elif short_code == 'ex':
            print("-"*50)
            print("Thank you for using Password Locker...")
            print("-"*50)
            break

        else:
            print("Sorry, That wasn't got. Please use the short codes\n")


if __name__ == '__main__':
    main()

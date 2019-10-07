import random
import string
import pyperclip

global users_list


class User:
    '''
    class to create user accounts and save their information
    '''
    # class Variables
    # global users_list
    users_list = []

    def __init__(self, first_name, last_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)


# class Credential:
#     '''
#     Class to create  account credentials, generate passwords and save their information
#     '''
#     # Class Variables
#     credentials_list = []
#     user_credentials_list = []

#     @classmethod
#     def check_user(cls, first_name, password):
#         '''
#         Method that checks if the name and password entered match entries in the users_list
#         '''
#         current_user = ''
#         for user in User.users_list:
#             if (user.first_name == first_name and user.password == password):
#                 current_user = user.first_name
#         return current_user

#     def __init__(self, user_name, site_name, account_name, password):
#         '''
#         Method to define the properties for each user object will hold.
#         '''

#         # instance variables
#         self.user_name = user_name
#         self.site_name = site_name
#         self.account_name = account_name
#         self.password = password

#     def save_credentials(self):
#         '''
#         Function to save a newly created user instance
#         '''
#     def test_copy_credential(self):
#         '''
#         Test to check if the copy a credential method copies the correct credential
#         '''
#         self.new_credential.save_credentials()
#         twitter = Credential('Ngigi', 'Twitter', 'works', 'pswd100')
#         twitter.save_credentials()
#         find_credential = None
#         for credential in Credential.user_credentials_list:
#             find_credential = Credential.find_by_site_name(credential.site_name)
#             return pyperclip.copy(find_credential.password)

#         Credential.copy_credential(self.new_credential.site_name)
#         self.assertEqual('pswd100', pyperclip.paste())
#         print(pyperclip.paste())
#         global users_list
#         Credential.credentials_list.append(self)

#     @classmethod
#     def display_credentials(cls, user_name):
#         '''
#         Class method to display the list of credentials saved
#         '''
#         user_credentials_list = []
#         for credential in cls.credentials_list:
#             if credential.user_name == user_name:
#                 user_credentials_list.append(credential)
#         return user_credentials_list

#     @classmethod
#     def find_by_site_name(cls, site_name):
#         '''
#         Method that takes in a site_name and returns a credential that matches that site_name.
#         '''
#         for credential in cls.credentials_list:
#             if credential.site_name == site_name:
#                 return credential

#     @classmethod
#     def copy_credential(cls, site_name):
#         '''
#         Class method that copies a credential's info after the credential's site name is entered
#         '''
#         find_credential = Credential.find_by_site_name(site_name)
#         return pyperclip.copy(find_credential.password)

import pyperclip
import random


class Credential:
    """
    Class that generates new instance of user's credentials
    """

    credentials_list = []

    def __init__(self, view_password, account, login, password):
        self.view_password = view_password
        self.account = account
        self.login = login
        self.password = password

    def save_credential(self):
        """
        save_credential method saves credential objects into the credential_list
        """
        Credential.credentials_list.append(self)

    def del_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in a number and returns a credential that matches that account name.
        Args:
            account: Account name to search for
        Returns :
            Credential of account that matches the account name.
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exist(cls, account):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        """
        display_credentials method that returns the credential list
        """
        return cls.credentials_list


class User:
    """
    Class that generates new instance of users
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """
        User.user_list.append(self)

    @classmethod
    def find_by_number(cls, username):
        '''
        Method that takes in a username and returns a user matched that username.
        Args:
            username: username to search for
        Returns:
            user that matched the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, characters):
        """
        user_exists method that checks is a user exists from the user list
        args:
        characters:password to search is nthe user exists 
        returns:
            boolean:true or false depending on the condition
        """
        for user in cls.user_list:
            if user.password == characters:
                return True

        return False

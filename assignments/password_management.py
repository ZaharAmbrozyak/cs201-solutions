import hashlib
import json
import re


class MyDB:
    """
        Our class to work with login system
    """

    def __init__(self) -> None:
        """
            We create instance attributes

            :attr:
                self.salt (str) - seryoga :)
                self.logged_in (bool) - contains the info if use has logged in
                self.cur_user (str) - contains username if we're logged in
                self.db_name (str) - json file name
                self.db (dict) - our DB to work with. id: [username, password]
                self.last_id (int) - tracks the length of our db

            :return:
                None
        """

        self.salt = 'seryoga'
        self.logged_in = False
        self.cur_user = None
        self.db_name = 'db.json'

        try:
            with open(self.db_name, 'r') as f:
                self.db = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.db = {}

        self.last_id = len(self.db)

    def _id_search(self, username: str):
        """
        Returns id of the user, or -1 if it does not exist in db

        :param
            username (str): username
        :return:
            int
        """

        for i in self.db:
            if self.db[i][0] == username:
                return i
        return -1

    def _username_check(self, username: str) -> bool:
        """
        Checks if argument username appears at db

        :returns:
            bool
        """

        for db_username, _ in self.db.values():
            if db_username == username:
                return True
        return False

    @staticmethod
    def _password_check(password: str, username: str) -> bool:
        """
        Method that checks if password is actually valid.
        Takes two arguments: password (really?) and username
        Requirements for the password:
        1. Has at least 1 big and small letter
        2. Has at least 1 number
        3. Has at least 1 special character
        4. Password length is between 8 and 99 characters
        5. Does not have username in it

        :param:
            password (str): user password to check.
            username (str): username
        :return:
            bool
        """

        pattern = re.compile(
            r"""
                ^
                (?=.*[a-z]) # має будь-які малі англійські буковки
                (?=.*[A-Z]) # має будь-які великі англійські буковки
                (?=.*\d) # має будь-які числа
                (?=.*[^\w\s]) # має символи, які не є ані буковками, ані числами
                .{8,99} # довжина від 8 до 99
                $
                """,
            re.VERBOSE)
        return bool(pattern.match(password)) and (username not in password)

    def change_user_name(self, new_username: str) -> None:
        """
        Method that changes old username to a new one if you're logged in

        :param
            new_username (str): new username
        :return:
            None
        """

        if self.logged_in:
            if not self._username_check(new_username):
                print(f'Username has been changed to {new_username}!')
                self.db[self._id_search(self.cur_user)][0] = new_username
                self.cur_user = new_username
            else:
                print("That username already exists in DB. Please choose another username!")
        else:
            print("You're not logged in!")

    def add_new_user(self, username: str, password: str) -> None:
        """
        Creates a new user and adds it to DB
        Takes two arguments: username and password.

        :param:
            username (str): username
            password (str): user password

        :return:
            None
        """

        if self._password_check(password, username):
            password_salt = password + self.salt
            if self._username_check(username):
                print("This username is not available")
            else:
                self.db[self.last_id] = [username, (str(hashlib.sha256(password_salt.encode()).digest()))]
                self.last_id += 1
                print("User has been added")
        else:
            print('That password is too weak lol')

    def search_user(self, username: str) -> None:
        """
        Method that searches user in self.db and takes one argument: user

        :param
            user (str): username

        :return:
            None
        """

        if self._username_check(username):
            print(f"That user exist in db, id {self._id_search(username)}")
        else:
            print("There's no such user in db")

    def show_users(self) -> None:
        """
        Method that simply prints out all keys at self.db

        :return:
            None
        """
        if self.logged_in:
            for username, _ in self.db.values():
                print(username)
            print("All users:")
        else:
            print("You're not allowed to do that. Please log in")

    def log_in(self, username: str, password: str) -> None:
        """
        Method that allows you to log_in. Takes two arguments: username and password

        :param:
            username (str): username
            password (str): password
        :return:
            None
        """

        if self._username_check(username):
            our_id = self._id_search(username)
            password_salt = password + self.salt
            encoded_password = str(hashlib.sha256(password_salt.encode()).digest())
            if self.db[our_id][1] == encoded_password:
                self.logged_in = True
                self.cur_user = username
                print(f"Log in was successful! Hello, {self.cur_user}!")
            else:
                print("Wrong user or password")
        else:
            print("There's no such user at DB")

    def log_out(self) -> None:
        """
        Method that is simply logs out from the system

        :return:
            None
        """
        if self.logged_in:
            print(f"You logged out! Goodbye, {self.cur_user}!")
            self.logged_in = False
            self.cur_user = None
        else:
            print("You did not log in tho?")


my_site = MyDB()


def mainloop() -> None:
    """
    Runs our mainloop console script

    :returns:
        None
    """
    text = ''' Write your commands :) :
        1. /add_user <user_name> <password>
        2. /search_user <user_name>
        3. /show_users
        4. /log_in <user_name> <password>
        5. /log_out
        6. /change_username <new_username>
        7. /exit
        '''
    print(text)
    command = ''
    while command != "/exit":
        try:
            command = input()
        except KeyboardInterrupt:
            command = "/exit"
        if command.startswith('/add_user'):
            _, user_name, user_password = command.split()
            my_site.add_new_user(user_name, user_password)
        elif command.startswith('/search_user'):
            _, user_name = command.split()
            my_site.search_user(user_name)
        elif command.startswith('/show_users'):
            my_site.show_users()
        elif command.startswith('/log_in'):
            _, user_name, user_password = command.split()
            my_site.log_in(user_name, user_password)
        elif command.startswith('/log_out'):
            my_site.log_out()
        elif command.startswith('/change_username'):
            _, new_username = command.split()
            my_site.change_user_name(new_username)
        elif command.startswith('/exit'):
            if my_site.logged_in:
                my_site.log_out()
            print('Bye-bye!')
        else:
            print("make sure you wrote your request correctly :)")


if __name__ == '__main__':
    mainloop()
    with open(my_site.db_name, 'w') as file:
        json.dump(my_site.db, file)
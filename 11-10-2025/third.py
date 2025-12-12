import json
output = {}

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
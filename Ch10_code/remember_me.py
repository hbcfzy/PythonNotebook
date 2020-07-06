"""welcome users"""

import json


def get_stored_username():
    """if the username has been stored, return the name, else none"""
    f_name = 'username.json'
    try:
        with open(f_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """get new username and write it into json file, return username"""
    username = input("Please imput your name: ")
    with open('username.json', 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def great_user():
    """great user with user's name"""
    username = get_stored_username()
    if username:
        print("Welcome back {}!".format(username.title()))
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}!".format(username))


if __name__ == "__main__":
    great_user()

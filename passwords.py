#! usr/bin/env python3
"""This script save the logins and passwords of some websites and e-mails
of the company. It's just a script for the transition of the IT team,
to not have any problems with passwords changed for them..

--Use mode--
'python passwords.py'
pgrm: Do you wanna save a login or read?
usr: [save/read]

Save
pgrm: Which login are you going to save?
usr: e-mail
pgrm: What is the login?
usr: e-mail@email.com
pgrm: What is the password?
usr: password

Read
pgrm: Which login do you wanna see?
usr: e-mail
pgrm rtn: THe login of e-mail is e-mail@email.com and the password is password.
"""

__version__ = "0.1.0"
__author__ = "Victor Soler"
__license__ = "Unlicense"

import os
import sys

data = {}
filepath = os.path.join("logins.txt")

user_answer = input("Do you want to save or read a login? [save/read] ").lower()

if user_answer == "read":
    # TODO: Print the available tags for user
    label_tag = input("Which tag? ").strip().lower().replace(" ", "")
    if label_tag == "":
        print("You must specify a tag.")
        sys.exit(1)
    try:
        for line in open(filepath):
            label, login, password = line.split("\t")
            if label_tag in label.lower():
                # TODO: Treat Label Desambiguation
                print(f"Label: {label}")
                print(f"Login: {login}")
                print(f"Password: {password}")
    except FileNotFoundError:
        logging.error(f"File {filepath} not found.")
        sys.exit(1)

elif user_answer == "save":
    while True:
        data = [
            input("Which is the label of this login?\n").strip().lower().replace(" ", ""),
            input("Login: "), 
            input("Password: "),
        ]
        with open(filepath, "a") as file_:
            file_.writelines("\t".join(data) + "\n")
        save_another = input("Do you want to save another login? [N/y] ").lower()
        if save_another == "n":
            print("\nCongratulations!!\nAll the logins has been saved.")
            break
        elif save_another == "y":
            continue
        else:
            print("You must entry an validated caracter: 'N' or 'y'.")
            sys.exit(1)
else:
    print("Incorrect use. You must write if do you want to read or save.")





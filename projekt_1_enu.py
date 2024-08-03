"""
project_1.py: first project for Engeto Online Python Academy

author: Pavel Dvořák
email: pavel.d@seznam.cz
discord: paveldv42
"""

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

import os
welcome = "TEXT ANALYZER"
separator = "=" * 70
separator2 = "-" * 70
separator3 = "_" * 70
verified = True
input_allowed = True
number_entered = True
correct_input_confirmation = True

# Defining functions...
def word_count(text):

    """This function finds the number of words in the given text and returns an int"""

    remove_newlines = text.replace("\n", " ")
    remove_whitespace = remove_newlines.strip()
    word_count = len(remove_whitespace.split(" "))
    
    return word_count

def starts_with_uppercase(text):
    uppercase_count = int(0)
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = remove_whitespace1.split()

    for word in create_list:
        if word[0].isupper() != True:
            uppercase_count
        else:
            word[0].isupper() == True
            uppercase_count += 1
    
    return uppercase_count

def only_uppercase_letters(text):
    uppercase = int(0)
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = remove_whitespace1.split()

    for word in create_list:
        if word.isupper() != True:
            uppercase
        elif word.isupper() == True and word.isalpha() != True:
            uppercase
        else:
            word.isupper() == True and word.isalpha() == True
            uppercase += 1
        
    
    return uppercase 

def only_lowercase_letters(text):
    lowercase = int(0)
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = remove_whitespace1.split()

    for word in create_list:
        if word.islower() != True:
            lowercase
        else:
            word.islower() == True
            lowercase += 1
    
    return lowercase 

def only_numbers(text):
    numbers = int(0)
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = remove_whitespace1.split()

    for word in create_list:
        if word.isdigit() != True:
            numbers
        else:
            word.isdigit() == True
            numbers += 1
    
    return numbers 

def sum_of_numbers_in_text(text):
    total_sum = int(0)
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = remove_whitespace1.split()

    for number in create_list:
        if number.isdigit() != True:
            total_sum
        else:
            number.isdigit() == True
            total_sum += int(number)
    
    return total_sum 

def character_count_graph(text):
    remove_newlines1 = text.replace("\n", " ")
    remove_whitespace1 = remove_newlines1.strip()
    create_list = sorted(len).remove_whitespace1.split()

def graph(text):
    removing_newlines = selected_text.replace("\n", " ")
    removing_dots = removing_newlines.replace(".", "")
    removing_commas = removing_dots.replace(",", "")
    removing_whitespace = removing_commas.strip()
    creating_list = removing_whitespace.split()
    creating_list.sort(key=len)
    longest_length = len(creating_list[-1]) + 3

    helper = 1
    total = 0

    for i in creating_list:
        if len(i) == helper:
            total += 1
        elif len(i) > helper:
            print(f"{str(len(i) - 1).rjust(2)}|{("*" * total).ljust(longest_length + 3)}|{total}")
            total = 1
            helper += 1
    print(f"{str(len(i)).rjust(2)}|{("*" * total).ljust(longest_length + 3)}|{total}")

os.system("clear")
print(separator)
print(welcome.center(70))
print(separator, "\n")

# Program execution...
while input_allowed and verified:
    while verified:
        user = input("Enter your username: ")
        if user not in registered_users:
            print(f"User {user.upper()} is not registered! Exiting the program...")
            input_allowed = False
            break
        elif user in registered_users:
            while verified:
                password = input("Enter your password: ")
                if registered_users[user] == password:
                    verified = False
                else:
                    print("Incorrect password! Try again...")
                    verified = True
    else:
        os.system("clear")
        print(separator)
        welcome2 = f"{user.upper()}, Welcome to the program: TEXT ANALYZER"
        print(welcome2.center(70))
        print(separator, "\n")
        print(f"Here are 3 texts for analysis:\n{separator3}\n\n1. {TEXTS[0].lstrip()}\n\n2. {TEXTS[1]}\n\n3. {TEXTS[2]}\n")
        print(separator3, "\n")
        
        
        while correct_input_confirmation:
            while number_entered:
                user_input = input("To select a text for analysis, enter a number between 1 and 3: ")
                if user_input.isdigit() == False:
                    print("A number was not entered! Exiting the program...")
                    number_entered = False
                    correct_input_confirmation = False
                    break
                elif user_input.isdigit() == True:
                    if int(user_input) < 1 or int(user_input) > 3:
                        print("A number between 1 and 3 was not entered! Exiting the program...")
                        number_entered = False
                        correct_input_confirmation = False
                        break
                    else:
                        number_entered = False
                        correct_input_confirmation = False
                        selected_text = (TEXTS[int(int(user_input) - 1)])
                        print(separator3)
                        print(f"\nThere are {word_count(selected_text)} words in the selected text.") 
                        print(f"There are {starts_with_uppercase(selected_text)} titlecase words.")
                        print(f"There are {only_uppercase_letters(selected_text)} uppercase words.")
                        print(f"There are {only_lowercase_letters(selected_text)} lowercase words.")
                        print(f"There are {only_numbers(selected_text)} numeric strings.")
                        print(f"The sum of all the number {sum_of_numbers_in_text(selected_text)}.")
                        print(f"{separator3}\n")
                        graph(selected_text)

print(f"\n{separator3}")
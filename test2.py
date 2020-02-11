import random
import os
import time

def generate_password(length_pass):
    # 33-126 diapazon symbols
    password = ''
    for i in range(length_pass):
        password += chr(random.randint(32,126))
    return password

def safe(input):
    if input != internal_password:
        # print('Wrong password', input)
        return False
    else:
        # print('OK')
        return True

def string_gen():
    string = ''
    for i in range(33,126):
        s = chr(i)
        string = s
        print("Generated password", internal_password, 'Trying password', string, 'Result:', safe(string))



def cls():
    print("\n" * 100)


def addition():

    string_for_addition = ''



internal_password = generate_password(8)

string_gen()
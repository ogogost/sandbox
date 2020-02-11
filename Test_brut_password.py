import random
import time

def generate_password(length_pass):
    # 33-126 diapazon symbols
    password = ''
    for i in range(length_pass):
        password += chr(random.randint(32,126))
    return password

def enter_password_engine(input):
    if input != internal_password:
        pass
        # print('Wrong password', input)
    else:
        print('OK', input)
        # break



def cracker(string):
    for i in range(33, 126):
        trying_pass = string + str(chr(i))
        enter_password_engine(trying_pass)
        if len(trying_pass) <= 4:
            cracker(trying_pass)
        else:
            break

internal_password = generate_password(4)
print('Generated password:', '"' + internal_password + '"')
begin = time.time()
stroka = ''
cracker(stroka)
end = time.time()
print('time:', end - begin)
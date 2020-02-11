def safe(input):
    flag_of_win = False
    if input != internal_password:
        # print('Wrong password', input)
        flag_of_win = False
        return False
    else:
        flag_of_win = True
        # print('OK')
        return True


def recursion():

    string = ''

    for i in range(33,126):
        string =  chr(i)
        print(string, safe(string))
        if safe(string) is False: continue
        else: break

def recursion_general():

    if flag_of_win is False:
        for i in range(33,126):
            string = chr(i) + chr(j)
            print(string, safe(string))
            if safe(string) is False:
                flag_of_win = False
                continue
            else:
                flag_of_win = True
                break


internal_password = '12345'
recursion()

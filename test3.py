

def recurs(string):

    for i in range(33,126):
        trying_pass = string + str(chr(i))
        # print(trying_pass)
        if len(trying_pass) <= 8:
            recurs(trying_pass)
        else:
            break



stroka = ''
recurs(stroka)
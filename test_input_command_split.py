
while True:
    user_input = input('command:').split()
    user_com = user_input[0]
    user_arg1 = user_input[1]
    user_arg2 = user_input[2]

    if user_com == 'sum':
        print(int(user_arg1) + int(user_arg2))
    elif user_com == 'mul':
        print(int(user_arg1) * int(user_arg2))

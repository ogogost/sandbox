import random

cash = 1000000
bit = 1
win = 0
print("Start money:", cash)
data = []
for rounds in range(20):
    for i in range (31):
        bit = bit * 2
        cash -= bit
        Red_black_flag = random.randint(0, 1)

        if bit >= cash:
            print('You loose!')
            data.append(i)
            continue
        if Red_black_flag == 0:
            win = 0
        elif Red_black_flag == 1:
            win = bit
        cash = cash + win - bit
        print('Round:', i, 'Win:', win, 'Flag:', Red_black_flag, 'Bit:', bit, 'Cash:', cash)


    print('Finish money:', cash)

print(data)
import random
value = 0
value_final = 0
for j in range(1,10):
    for i in range(1, 1000000):
        r_value = random.randint(0, 1)
        value += r_value
        value_final = value / i

    print(value_final)
    value = 0
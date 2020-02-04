import time


def is_leap2(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: leap = True
            else: leap = False
        else: leap = True
    else: leap = False
    return leap

n = 100000


def circle():

    begin = time.time()
    for i in range(n):
        is_leap(n)
    timer_1 =time.time() - begin

    begin = time.time()
    for i in range(n):
        is_leap2(n)
    timer_2 = time.time() - begin

time_1_counter = 0
time_2_counter = 0
timer_1 = 0
timer_2 = 0
count = 100

while count != 0:
    circle()
    time_1_counter += timer_1
    time_2_counter += timer_2
    count -= 1

print(time_1_counter)
print(time_2_counter)
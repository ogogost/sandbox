def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: leap = True
            else: leap = False
        else: leap = True
    else: leap = False
    return leap


print("1988" ,is_leap(1988))
print("1899" ,is_leap(1899))
print("1900" ,is_leap(1900))
print("2000" ,is_leap(2000))
print("2100" ,is_leap(2100))

while True:
    print("Main circle")
    flag = 1
    while flag == 1:
        print("Second circle")
        if input("Input:") == "1":
            continue
        else:
            print("End of Second circle")
            flag = 0
    print("Continue of Main circle")
    break
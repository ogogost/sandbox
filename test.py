data = ['a10', 'a8', 'aj', 'aq']
count = data

# def new(arg):
for i in range(len(data)):
    count[i] = data[i][1:3]

# new(data)
print(count)
n = 1
names = []

while True:
    try:
        names.append(input())
        if len(names) == 2:
            print(f'Case {n}: {names.pop()}, {names.pop()}')
            n += 1
    except:
        break
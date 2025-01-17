N = int(input())
f = 5**N
f = str(f)
print('0.', end='')
for _ in range(N-len(f)):
    print('0', end='')
print(f)
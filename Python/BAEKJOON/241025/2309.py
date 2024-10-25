import sys

dwarfs = [0]*9
for i in range(9):
    dwarfs[i] = int(sys.stdin.readline())
dwarfs.sort()
target = sum(dwarfs)-100
first, second = 0, 0
for j in range(9):
    for k in range(9):
        if dwarfs[j]+dwarfs[k] == target:
            first, second = j, k
            break
    if first:
        break
for l in range(9):
    if l == first or l == second:
        continue
    print(dwarfs[l])
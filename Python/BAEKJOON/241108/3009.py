coordinate = [[] for _ in range(2)]
for _ in range(3):
    x, y = map(int, input().split())
    coordinate[0].append(x)
    coordinate[1].append(y)
for i in range(3):
    if coordinate[0].count(coordinate[0][i]) == 1:
        a = coordinate[0][i]
    if coordinate[1].count(coordinate[1][i]) == 1:
        b = coordinate[1][i]
print(a, b)
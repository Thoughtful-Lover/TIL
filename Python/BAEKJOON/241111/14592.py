N = int(input())
attendants = [[] for _ in range(3)]
for _ in range(N):
    a, b, c = map(int, input().split())
    attendants[0].append(a)
    attendants[1].append(b)
    attendants[2].append(c)
if attendants[0].count(max(attendants[0])) == 1:
    print(attendants[0].index(max(attendants[0]))+1)
elif attendants[1].count(max(attendants[1])) == 1:
    print(attendants[1].index(max(attendants[1]))+1)
else:
    print(attendants[2].index(max(attendants[2]))+1)
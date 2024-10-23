T = int(input())
for _ in range(T):
    n, p = map(int, input().split())
    print(n, p)
    print(n*p-(n-1)*2)
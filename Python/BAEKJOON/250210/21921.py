N, X = map(int, input().split())
visitors = list(map(int, input().split()))
while True:
    if not max(visitors):
        print('SAD')
        break
    visit = 0
    top_visit = 0
    cnt = 1
    for i in range(X):
        visit += visitors[i]
    top_visit = visit
    for j in range(X, N):
        visit -= visitors[j-X]
        visit += visitors[j]
        if top_visit<visit:
            top_visit = visit
            cnt = 1
        elif top_visit == visit:
            cnt += 1
    print(top_visit)
    print(cnt)
    break
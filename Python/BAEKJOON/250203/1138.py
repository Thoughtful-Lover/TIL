N = int(input())
memory = list(map(int, input().split()))
answer = [0]*N
for i in range(N):
    if i == 0:
        answer[memory[i]] = 1
    elif not memory[i]:
        answer[i+1] = i+1
    else:
        cnt = 0
        for j in range(N):
            if answer[j] > i+1:
                cnt += 1
            if cnt == memory[j]:
                answer[j] = i+1
print(*answer)
'''
1764. 듣보잡

듣도 못한 사람 명단과 보도 못한 사람 명단이 주어질 때
듣도 보도 못한 사람의 명단

N: 듣도 못한 사람 수
M: 보도 못한 사람 수
찻쩨즐에 중복되는 이름의 수
'''

from collections import deque

# N: 듣도 못한 사람 수, M: 보도 못한 사람 수
N, M = map(int, input().split())
# 이름의 입력 값들을 저장할 리스트 names
names = [0] * (N+M)
# 듣도 보도 못한 사람 수 cnt
cnt = 0

# names에 모든 이름들을 입력 받고, 오름차순으로 정리
for i in range(N+M):
    name = input()
    names[i] = name
names.sort()

# 이름들을 검사할 데크 q, 와 같은 이름들을 저장해줄 데크 same_names
q = deque()
same_names = deque()
# names를 순회하며
for n in names:
    # q에 뭐가 있을 때 q에서 하나를 뺐는데, 만약 연속된 2개가 동등하면
    # 같은 이름이므로 cnt를 1 증가하고 해당 이름을 같은 이름들의 데크에 저장
    if q and q.pop() == n:
        cnt += 1
        same_names.append(n)
    # 위 조건이 아니라면 이름들을 q에 저장
    else:
        q.append(n)

# 듣도 보도 못한 사람의 수를 출력하고
# 듣도 보도 못한 사람의 명단을 차례로 출력
print(cnt)
for same_name in same_names:
    print(same_name)
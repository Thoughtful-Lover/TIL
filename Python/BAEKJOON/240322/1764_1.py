'''
1764. 듣보잡

듣도 못한 사람 명단과 보도 못한 사람 명단이 주어질 때
듣도 보도 못한 사람의 명단

N: 듣도 못한 사람 수
M: 보도 못한 사람 수
찻쩨즐에 중복되는 이름의 수
'''

'''
이거는 시간초과됨
'''

# N: 듣도 못한 사람 수, M: 보도 못한 사람 수
N, M = map(int, input().split())
# 이름의 입력 값들을 저장할 리스트 n_names, m_names
n_names = [0] * N
m_names = [0] * M
# 듣도 보도 못한 사람 수 cnt
cnt = 0
# 같은 이름을 저장해줄 리스트 same_names
same_names = []

# n_names 에 이름들 저장
for i in range(N):
    n_name = input()
    n_names[i] = n_name

# m_names 에 이름들 저장
for j in range(M):
    m_name = input()
    m_names[j] = m_name

# 만약 n_names의 이름들 중 같은 이름이 m_names에도 있으면
for name in n_names:
    # cnt를 1 증가하고, same_names에 중복되는 이름을 append
    if name in m_names:
        cnt += 1
        same_names.append(name)
# same_names 를 정렬
same_names.sort()

# 출력 조건에 따라 출력
print(cnt)
for sn in same_names:
    print(sn)

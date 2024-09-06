'''
11399. ATM

ATM 1대
ATM 앞에 N명의 사람들
사람들은 1~N번, i번 사람이 돈을 인출하는데 걸리는 시간 Pi분
사람들이 최소로 기다리게 하려면?
'''


# 사람수 N과 사람들의 이용시간 정보를 당은 리스트 people을 입력 받고
N = int(input())
people = list(map(int, input().split()))
# 사람들이 걸리는 시간을 정렬
people.sort()
# 사람들이 사용하는데 걸리는 시간을 저장할 변수 min_sum
min_sum = 0

# 리스트 내를 순회하며, 앞에 사람이 이용하는 만큼 뒤에 사람들 전원이 기다려야 하므로,
# i번째 사람은 전체 N에서 자신의 번호까지를 제외한 뒷사람을 기다리게 만든다.
for i in range(N):
    min_sum += people[i]*(N-i)

print(min_sum)
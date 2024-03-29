'''
2562. 최댓값
9개의 서로 다른 자연수가 주어질 때
이들 중 최댓값을 찾고, 그 최댓값이 몇 번째 수인지를 구하는 프로그램
'''

# 최대값과 몇 번째 수인지를 저장해 줄 리스트 max_num 을 정의. 이때 N은 자연수이고 1번째부터 시작하므로, 각각 0을 초기값으로 지정
max_num = [0, 0]

# 총 9번 시행하며
for i in range(1, 10):
    N = int(input())
    # 입력 받은 수가 max_num 에 저장된 수보다 크면, 최대값과 몇 번째 수인지를 갱신해준다.
    if max_num[0] < N:
        max_num[0] = N
        max_num[1] = i

for j in range(2):
    print(max_num[j])
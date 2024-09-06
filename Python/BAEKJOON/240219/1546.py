'''
1546. 평균

성준이의 점수 중 최고값을 M
점수 = (점수/M) * 100
새로운 평균을 구하라
'''


# 점수의 개수 N
N = int(input())
# 받은 점수들의 리스트
array = list(map(int, input().split()))
# 최고점 M
M = max(array)

# 새로운 점수를 만들어줌
for i in range(N):
    array[i] = array[i]/M * 100

# 평균을 출력
print(sum(array)/len(array))
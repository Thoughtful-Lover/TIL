'''
11047. 동전 0
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

# 1차시도_시간 초과 => sys로 입력해보려고 함
import sys

# 동전의 개수 N과 목표값인 K를 입력 받음
N, K = map(int, sys.stdin.readline().split())
# 동전의 정보를 저장할 배열 coins를 정의
coins = [0]*N
# coins에 동전의 정보를 저장
for i in range(N):
    coins[i] = int(sys.stdin.readline())
# 계산할 정보의 현재 인덱스를 저장할 변수 j와 사용한 동전 개수를 저장할 변수 cnt, 큰값부터 빼가야하므로 -1에서 시작
j = -1
cnt = 0
# 계산할 값이 0보다 클 때, 즉 0이 될 때까지 시행
while K > 0:
    # 만약 현재 선택된 동전이 남은 값보다 적으면
    if coins[j] > K:
        # 동전을 한 단계 줄여주고 다시 처음으로 돌아감
        j -= 1
        continue
    # 만약, 위 조건에 걸리지 않는다면, 현재 동전 값으로 뺄 수 있는 만큼 횟수를 더해주고 해당 값만큼 뺀 값으로 K를 갱신, j를 1 감소
    cnt += K//coins[j]
    K %= coins[j]
    j -= 1
# 위 반복문이 종료되면 최종적인 cnt를 출력해줌
print(cnt)
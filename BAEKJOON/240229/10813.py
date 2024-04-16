'''
10813. 공 바꾸기

도현이는 1~N번까지 적힌 바구니 N개
바구니에는 바구니 번호와 같은 번호가 적힌 공
M번 공을 바꾸는데 공을 바꿀 바구니 2개를 선택하고 두 바구니 속 공을 교환

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)
둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법
각 방법은 두 정수 i j
1 ≤ i ≤ j ≤ N
'''

# 바구니의 개수 N, 교환의 횟수 M
N, M = map(int, input().split())
# 바구니를 표현한 baskets
baskets = [0] * N
# 인덱스로 접근하되 들어가 있는 값은 인덱스 + 1
for balls in range(N):
    baskets[balls] = balls+1

for changes in range(M):
    # 교환행위도 인덱스로 접근하므로 입력받은 값에서 -1 하여 교환 시행
    i, j = map(int, input().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(*baskets)
'''
10811. 바구니 뒤집기

도현이는 1~N번까지 적힌 바구니
M번 바구니의 순서를 역순으로 바꾼다.
한 번 바꿀 때 범위 내의 바구니를 역순으로
바구니에 적혀 있는 번호를 왼쪽부터 출력

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)
둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법
'''

# 바구니의 번호 N, 바구니를 역순으로 바꾸는 시행의 횟수 M
N, M = map(int, input().split())
# 바구니에 1부터 N까지 수를 배정
baskets = [num for num in range(1, N+1)]
# 역순으로 바꾸는 시행을 M번만큼
for change_num in range(M):
    i, j = map(int, input().split())
    # 홀수일 때는 가운데를 제외한 양쪽의 수를 바꿔서 역순을 만들어주고
    # 짝수일 때는 양쪽의 수를 바꿔서 역순을 만들어줌
    for change in range((j-i+1)//2):
        baskets[i-1+change], baskets[j-1-change] = baskets[j-1-change], baskets[i-1+change]

print(*baskets)

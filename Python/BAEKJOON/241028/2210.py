# 데큐를 import
from collections import deque


# 숫자를 찾는 함수 making_numbers
# y와 x는 현재 위치, num은 현재까지 만든 숫자, cnt는 현재까지 붙인 숫자의 개수
def making_numbers(y, x, num, cnt):
    # 현재 위치에서 숫자판에 있는 값을 num에 추가해주고
    num += board[y][x]
    # 만약 숫자 값이 6이 되었을 때
    if cnt == 6:
        # 만든 숫자가 기존에 만들지 않은 새로운 숫자면
        if num not in numbers:
            # 그 숫자를 numbers에 넣는다.
            numbers.append(num)
        # 그리고 아무튼 함수 끝
        return
    # 델타로 상하좌우 이동
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni, nj = y+di, x+dj
        # 이동할 값이 숫자판의 범위 내에 위치하면
        if 0<=ni<5 and 0<=nj<5:
            # 새로운 위치와, 기존에 만든 숫자를 넘기고, 붙이는 숫자의 수는 1 증가
            making_numbers(ni, nj, num, cnt+1)


# 숫자판 정보를 2차원 배열 형태로 board에 저장
# 이때 나중에 숫자를 이어붙이기 편하게 하기 위해 개별 원소 값은 string 현태로 입력 받는다
# 입력 값이 공백을 두고 있으므로 input() 뒤에 꼭 split() 넣어주기
board = [list(input().split()) for _ in range(5)]
# 완성된 6자리 숫자를 저장할 numbers를 정의
numbers = deque()
# 전체를 순회하며
for i in range(5):
    for j in range(5):
        # 숫자를 만드는 함수에 집어 넣음
        making_numbers(i, j, '', 1)
# 위의 반복이 완료되면 number네 담긴 원소의 개수를 출력
print(len(numbers))
'''
5658. 보물상자 비밀번호

각 변에는 동일한 개수의 숫자 시계방향순으로 높은 자리 수
4개의 변
보물 상자에는 자물쇠, 이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수
N개의 숫자가 입력으로 주어졌을 때, 보물 상자의 비밀번호를 출력하는 프로그램
'''


from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = deque(input())
    passwords = deque()
    for _ in range(N-1):
        for i in range(4):
            password = ''
            for j in range(N):
                password += numbers[i*4+j]
            password = int(password, 16)
            passwords.append(password)
        numbers.append(numbers.popleft())
    passwords = set(passwords)
    passwords = list(passwords)
    passwords.sort(reverse=True)
    print(f'#{tc} {passwords[K-1]}')

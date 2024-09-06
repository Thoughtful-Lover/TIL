'''
9216. Hello Judge

N개의 테스트케이스들에게 N개의 줄에 걸쳐 "Hello World, Judge i!"를 출력
i는 줄의 번호
'''


# N을 입력 받고
N = int(input())
# 범위 1~N만큼 주어진 문구를 출력해줌
for i in range(1, N+1):
    # f-string을 활용
    print(f'Hello World, Judge {i}!')
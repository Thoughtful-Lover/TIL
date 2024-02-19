'''
3003. 킹, 퀸, 룻, 비숍, 나이트, 폰

킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

입력하면 몇 개를 더하거나 빼야 하는지 출력
'''


# 체스의 원래 개수를 chess 리스트로 만들기
chess = [1, 1, 2, 2, 2, 8]

# 내가 현재 가진 개수를 my 리스트로 만들기
my = list(map(int, input().split()))

# chess 에서 my 를 빼주면 올바른 세트에 필요한 숫자가 나온다.
for i in range(6):
    chess[i] -= my[i]

print(*chess)

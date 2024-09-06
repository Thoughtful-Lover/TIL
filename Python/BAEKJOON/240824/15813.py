'''
15813. 너의 이름은 몇 점이니?

첫째 줄에 이름의 길이
둘째 줄에 이름

A = 1점
부터 1점씩 높아져서
Z = 26점

이름 점수를 출력
'''

# 이름 점수를 저장할 변수 name_score
name_score = 0

# 문제에서 주어진 입력을 받고
n = int(input())
name = list(input())

# 이름을 순회하며
for char in name:
    # 각 철자를 점수로 변환해서 name_score에 저정
    # 대문자 A는 아스키 코드로 64이므로 아스키코드로 변환한 값에서 63씩 빼면 문제 조건에 맞는 점수가 됨
    name_score += ord(char)-64

# 최종적으로 저장된 name_score를 출력
print(name_score)
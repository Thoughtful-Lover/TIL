'''
9012. 괄호
'('와 ')'로 이루어진 괄호 문자열
괄호의 모양이 바르게 구성된 문자열 = 올바른 괄호문자열

테스트 케이스 T개
올바른 괄호 문자열이면 yes
아니면 No
'''

# 테스트 케이스 T 입력
T = int(input())
# 총 T개의 문자열을 입력 받되
for _ in range(T):
    # 리스트 형태로 입력 받고, 왼쪽 괄호의 개수를 left에 오른쪽 괄호의 개수를 right에 저장
    bracket_list = list(input())
    left = 0
    right = 0
    # 리스트를 순회
    for char in bracket_list:
        if char == '(':
            left += 1
        else:
            right += 1
        # 단 오른쪽 괄호의 개수가 왼쪽 괄호보다 많으면 괄호의 모양이 바르게 구성되지 않으므로 중단
        if right > left:
            break
    # 왼쪽과 오른쪽의 개수가 같으면 올바른 괄호
    # 끝까지 모두 세든, 도중에 멈췄던 양쪽의 개수가 같지 않으면 올바르지 않음
    if left == right:
        print('YES')
    else:
        print('NO')

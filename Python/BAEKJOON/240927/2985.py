'''
2985. 세수

세 수가 주어졌을 때
수식에 맞게 출력
'''

# 하드 코딩 가보자
A, B, C = map(int, input().split())
if A+B == C:
    print(f'{A}+{B}={C}')
elif A-B == C:
    print(f'{A}-{B}={C}')
elif A*B == C:
    print(f'{A}*{B}={C}')
elif A/B == C:
    print(f'{A}/{B}={C}')
elif A == B+C:
    print(f'{A}={B}+{C}')
elif A == B-C:
    print(f'{A}={B}-{C}')
elif A == B*C:
    print(f'{A}={B}*{C}')
elif A == B/C:
    print(f'{A}={B}/{C}')
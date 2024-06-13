'''
21598. SciComLove

첫 줄에 정수 N이 주어집니다.
"SciComLove"를 예제와 같이 N번 출력합니다.
단, 따옴표는 출력하지 않습니다
'''

# N을 입력 받아 횟수만큼 출력
N = int(input())
for _ in range(N):
    print('SciComLove')

# 또는 명시적으로 조건을 구분하는 방법도 있다. 1<=N<=2이므로
'''
N = int(input())
if N == 1:
    print('SciComLove')
else:
    print('SciComLove')
    print('SciComLove')    
'''
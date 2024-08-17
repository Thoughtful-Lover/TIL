'''
10995. 별 찍기 - 20

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 차례대로 별을 출력한다.

if N == 1:
*

2
* *
 * *

3
* * *
 * * *
* * *

4
* * * *
 * * * *
* * * *
 * * * *
'''


# N을 입력 받음
N = int(input())
# N 행만큼 별을 찍는데
for i in range(1, N+1):
    # 홀수번째 행에서는 맨 앞 칸부터 별 한 칸, 공백 한 칸씩 N개의 별을 찍고
    if i%2 == 1:
        for _ in range(N):
            print('* ', end='')
    # 짝수번째 행에서는 맨 앞 칸부터 공백 한 칸, 별 한 칸씩 N개의 별을 찍는다.
    elif i%2 == 0:
        for _ in range(N):
            print(' *', end='')
    # 각 행의 출력을 마치면 end 옵션을 초기화해준다.
    print()
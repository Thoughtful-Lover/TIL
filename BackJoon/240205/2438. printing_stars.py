'''
2438. 별 찍기 - 1

문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''
N = int(input()) # 1 <= N <= 100

for i in range(1, N+1): # 입력된 수의 범위 내에서
    for j in range(1, i+1): # 각각의 수만큼 *을 출력
        print('*', end='')
    print()
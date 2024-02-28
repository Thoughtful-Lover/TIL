'''
2439. 별 찍기 -2

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
'''


N = int(input())

# N 번 만큼 출력을 하되
for i in range(N):
    # 공백은 1씩 감소하며
    for j in range(N-1-i):
        print(' ', end = '')
    # '*' 은 1씩 증가하며 출력
    for k in range(1+i):
        print('*', end = '')
    print()
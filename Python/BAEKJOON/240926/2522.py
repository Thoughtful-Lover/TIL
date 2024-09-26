'''
2522. 별 찍기 - 12

예제를 보고 규칙을 유추한 뒤에 별을 찍으시오.

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

if (input == 3) {
    return(
          *
         **
        ***
         **
          *
    )
}
'''

N = int(input())
for i in range(1, N+1):
    for _ in range(N-i):
        print(' ', end='')
    for _ in range(i):
        print('*', end='')
    print()
for j in range(1, N):
    for _ in range(j):
        print(' ', end='')
    for _ in range(N-j):
        print('*', end='')
    print()
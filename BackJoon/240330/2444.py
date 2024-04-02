'''
2444. 별 찍기 - 7

예제를 보고 규칙을 유추한 뒤에 별을 찍어보세요

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.


예제 입력 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''


def diamond_start(n):
    for i in range(1, N*2):
        if i < N:
            for _ in range((N*2-i)//2):
                print(' ', end='')
            for _ in range(i):
                print('*', end='')
            for _ in range((N*2-i)//2):
                print(' ', end='')
            print()
        elif i == N:
            for _ in range(N):
                print('*', end='')
                print()
                continue
        else:
            for _ in range((N * 2 - (i % N) - 1) // 2):
                print(' ', end='')
            for _ in range(i % N):
                print('*', end='')
            for _ in range((N * 2 - (i % 5) - 1) // 2):
                print(' ', end='')
            print()


N = int(input())
diamond_start(N)
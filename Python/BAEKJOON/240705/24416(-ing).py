'''
24416. 알고리즘 수업 - 피보나치 수 1

재귀호출과 동적 프로그래밍을 활용할 때
각각의 실행 횟수를 출력
'''

cnt = 0
caunt = 0


def fib(n):
    global cnt 
    cnt += 1
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))


def fibonacci(n):
    f = [1, 1]


n = int(input())
fib(n)

print((cnt+1)//2, 2*n-2)

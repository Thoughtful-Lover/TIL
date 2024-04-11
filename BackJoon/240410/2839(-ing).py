'''
2839. 설탕 배달

상근이는 3킬로그램과 5킬로그램으로 설탕을 배달
Nkg을 배달하려 할때
최대한 적은 봉지를 가져가려할 때
그 수를 구하시오
정확히 N킬로그램을 만들 수 없다면 -1을 출력
'''


def sugar(target):
    if target%5 == 0:
        print(target//5)
    elif target%5%3 == 0:
        print(target//5+target%5//3)
    elif target%3%5 == 0:
        print(target//3+target%3//5)
    elif target%3 == 0:
        print(target//3)
    else:
        print(-1)


N = int(input())
sugar(N)
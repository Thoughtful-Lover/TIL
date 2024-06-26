'''
2117. 홈 방범 서비스

N*N 크기의 도시에 홍방범 서비스를 제공
마름모 형태로 제공

서비스 영역의 크기 K가 커질수록 운영 비용이 커진다.
운영비용은 서비스 영역의 면적과 동일
운영 비용 = K*K + (K-1)*(K-1)
도시를 벗어난 영역에 서비슬 레공해도 운영 비용은 변경되지 않는다.

도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
손해를 보지 않으면서 홍방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고
그 때의 홈방범 서비스를 제공 받는 집들의 수를 출력하는 프로그램
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
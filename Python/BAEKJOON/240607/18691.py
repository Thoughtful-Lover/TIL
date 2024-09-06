'''
18691. Pokemon Buddy

포켓몬은 걸으면서 사탕을 얻음
1, 3, 5km 당 사탕을 얻음

G, C, E
G: Pokemon 그룹
C: 현재 가진 사탕 수
E: 목표 사탕 수

앞으로 걸어야할 km 수를 출력하라
'''


T = int(input())
# 각 테스트 케이스별 시행
for _ in range(T):
    # G는 그룹의 유형, C는 현재 가진 사탕의 수, E는 진화에 필요한 사탕의 수
    G, C, E = map(int, input().split())
    # 가진 사탕이 진화하는데 필요한 양과 같거나 많으면 0을 출력
    if C >= E:
        print(0)
        continue
    # 그룹 1이면 1km 당 사탕 1개
    elif G == 1:
        print(E-C)
    # 그룹 2이면 1km 당 사탕 3개
    elif G == 2:
        print((E-C)*3)
    # 그룹 3이면 1km 당 사탕 5개
    elif G == 3:
        print((E-C)*5)
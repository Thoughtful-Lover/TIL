'''
20254. Site Score

최소한 한 문제를 풀 수 있는 팀을 기준으로 점수를 산정
대회별 점수 가중치에 따라서 총점을 출력
56a, 24b, 14c, 6d
'''

a, b, c, d = map(int, input().split())
print(56*a+24*b+14*c+6*d)
'''
4999. 아!

첫째줄 자신의 낼 수 있는 가장 긴 aaah
둘째줄 의사가 요구하는 aaah

자기가 낼 수 있는 길이의 의사 go
아니면 no
'''


JH = input()
doctor = input()

# 의사가 요구하는 길이가 낼 수 있는 길이보다 길면 no 출력
if len(JH) < len(doctor):
    print('no')
# 나머지 경우 go 출력
else: print('go')
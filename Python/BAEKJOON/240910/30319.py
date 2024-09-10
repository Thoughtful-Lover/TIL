'''
31319. Advance to Taoyuan Regional

문제 정확히는 이해 안되는데,
무슨 행사가 2023/10/21 - 20/23 까지 열리는데
35일 전에는 신청을 해야 하나봐
그래서 신청 일자를 봤을 때
이 조건에 맞으면 GOOD을 출력
너무 늦었다면 TOO LATE를 출력

입력 양식은 'YYYY-MM-DD'

이 때,
YYYY는 무조건 2023
MM은 1~12
DD는 1~28
'''


# '-' 구분자를 기준으로 각각 연, 월, 일 값을 y, m, d에 저장
y, m, d = map(int, input().split('-'))
# 10/21일을 일로 환산하면 10*28+21=301, 301-35 = 266
if m*28+d <= 266:
    print('GOOD')
else:
    print('TOO LATE')

'''
19602. Dog Treats

간식을 좋아하는 개 Barley는 그날 받은 간식의 크기에 따라 서로 다른 행복을 느끼며 그 수식은 아래와 같다.
1 × S + 2 × M + 3 × L
만약 총 행복의 값이 10이상이면 Barley는 행복하고 그렇지 않으면 슬프다

각각 S, M, L 의 행복을 주는 간식의 수치가 차례로 주어진다.
해당 값을 바탕으로 Barley 가 행복하면 happy, 슬프면 sad 를 출력한다.
'''

S = int(input())
M = int(input())
L = int(input())
happiness = 1*S + 2*M + 3*L
if happiness >= 10:
    print('happy')
else:
    print('sad')
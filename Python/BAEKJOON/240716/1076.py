'''
1076. 저항

저항은 색 3개를 이용해 저항이 몇 옴인지 나타낸다
첫 번째 나온 수는 값*10해서 더해주고, 두 번째 나온 색은 값을 더하고, 마지막 색은 곱해야 한다.
'''


# 저항 값과 곱에 대한 정보를 딕셔너리 형태로 만들어준다.
resistance_info = {
    'black': (0, 1),
    'brown': (1, 10),
    'red': (2, 100),
    'orange': (3, 1000),
    'yellow': (4, 10000),
    'green': (5, 100000),
    'blue': (6, 1000000),
    'violet': (7, 10000000),
    'grey': (8, 100000000),
    'white': (9, 1000000000)
}
# 저항값을 저장할 변수 resistance
resistance = 0
# 조건에 따라 구현한다.
for i in range(3):
    color = input()
    if i == 0:
        resistance += resistance_info[color][0]*10
    elif i == 1:
        resistance += resistance_info[color][0]
    elif i == 2:
        resistance *= resistance_info[color][1]
print(resistance)
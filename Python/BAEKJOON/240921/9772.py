'''
9772. Quadrants

(x, y) 좌표가 주어질 때
해당 좌표가 어느 사분면에 위치했는지 출력
Q1, Q2, Q3, Q4
만약 x축이나 y축에 있는 좌표라면 AXIS를 출력
'''

# 입력 값의 수가 정해져 있지 않으므로 try, except 문을 활용
while True:
    try:
        # 좌표 값이므로 float 값이 들어올 수도 있음
        x, y = map(float, input().split())
        # 둘 중에 하나라도 x축 상이나 y축 상에 걸친 경우
        if not x or not y:
            print('AXIS')
        # 1사분면
        elif y>0 and x>0:
            print('Q1')
        # 2사분면
        elif y>0 and x<0:
            print('Q2')
        # 3사분면
        elif y<0 and x<0:
            print('Q3')
        # 4사분면
        elif y<0 and x>0:
            print('Q4')
    except:
        break
'''
1598. 꼬리에 꼬리를 무는 숫자 나열

4줄짜리 표에 왼쪽부터 수를 아래로 1부터 순서대로 적어낸다
두 수가 주어질 때 동서방향거리와 남북방향거리의 합인 직각거리를 구해서 출력
'''


# 두 수를 입력 받았을 때
a, b = map(int, input().split())
# 두 수의 x좌표는 두 수를 4로 나눈 몫
# 이 때, 4의 배수인 값은 몫보다 1 적은 x좌표에 위치해 있으므로 각각의 값에서 1을 빼주고 몫을 계산
row = abs((a-1)//4-(b-1)//4)
# 두 수의 y좌표는 두 수를 4로 나눈 나머지
a_cloumn = a%4
b_column = b%4
# 하지만 몫을 기준으로 계산할 경우 4의 배수인 값은 0이 되므로, 0인 경우 그 값을 4로 바꿔줌
if not a_cloumn:
    a_cloumn = 4
if not b_column:
    b_column = 4
column = abs(a_cloumn-b_column)
print(row+column)
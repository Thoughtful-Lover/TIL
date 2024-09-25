'''
20233. Bicycle

자전거를 타려고 하는데 두 개의 한달 요금제가 있다.
- 월 a 루블, 매일 30분씩 무료, 이후로는 분당 x 루블
- 월 b 루블, 매일 45분씩 무료, 이후로는 분당 y 루블

11월은 총 21일이고 너는 하루에 T 분 자전거를 탄다

각각의 요금제를 선택했을 시,  총 얼마씩의 요금을 지불하게 될지 출력

정수 a, x, b, y ( 0<=a,x,b,y<=100)
마지막 줄에는 T  (1<=T<=1440)
'''

# 각각의 값을 입력 받고
a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
# (하루 사용 시간-무료 사용 시간)*(분당 요금)*21 해줌
# 단 하루 사용 시간이 무료 사용 시간보다 작은 경우, 월정액만 지불하면 됨
print(a if T<=30 else a+(T-30)*x*21 , b if T<=45 else b+(T-45)*y*21)
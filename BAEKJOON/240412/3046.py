'''
3046. R2
S = (R1+R2)/2
R1과 S가 주어질 때, R2를 출력하시오
'''


# map 함수를 이용해 두 변수를 각각 입력 받는다.
R1, S = map(int, input().split())
# S를 구하는 공식을 이항해서 R2를 구하는 공식을 만든다.
R2 = S*2 - R1
print(R2)
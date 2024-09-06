'''
31403. A + B - C

해당 수를 정수형으로 인식할 때와, 문자열로 인식할 때의 결과 값을 각각 출력하시오.
'''

A = int(input())
B = int(input())
C = int(input())
sA = str(A)
sB = str(B)

print(A+B-C)
# 파이썬에서 문자열끼리의 뺄셈이 안되므로, 덧셈만 문자열끼리 해주고 뺄셈은 정수형으로 바꿔주어 뺀다.
print(int(sA+sB)-C)
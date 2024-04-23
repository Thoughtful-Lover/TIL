'''
1427. 소트인사이드

배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

'''


# 문자열 리스트로 입력 받음
N = list(input())
# 내림차순으로 정렬, reverse=True 이면 내림차순이다.
N.sort(reverse=True)
# 나란히 한자씩 프린트 해주고
for num in N:
    print(num, end='')
# 프린트 end 초기화
print()
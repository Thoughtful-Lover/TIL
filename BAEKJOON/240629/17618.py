'''
17618. 신기한 수

신기한 수 : 모든 자릿수의 합으로 나누어지는 수
N이 주어지면
N 이하의 정수 중 신기한 수의 개수를 출력
'''

# 당연히 N >= 1,000,000 이 넘어가니 시간초과가
'''# N을 입력 받고
N = int(input())
# 신기한 수를 저장할 변수 cnt
cnt = 0
while N > 0:
    # N을 문자열로 바꿔주고
    n = str(N)
    # 각 자리수의 합을 저장해줄 변수 calculate 를 정의
    calculate = 0
    # n을 순회하며 각 자리수를 calculate에 더해줌
    for num in n:
        calculate += int(num)
    # 그리고 원래의 수를 더한 값으로 나눈 나머지가 0이면
    if N%calculate == 0:
        # cnt를 1 증가
        cnt += 1
    # N을 1 감소
    N -= 1
# 반복문이 종료되면 cnt를 출력
print(cnt)'''


# 여전히 시간초과.. 뭔가 접근법을 달리 해야하나봐
'''N = int(input())
cnt = 0
while N > 0:
    n = map(int, list(str(N)))
    if N%sum(n) == 0:
        cnt += 1
    N -= 1
print(cnt)'''

# pypy로 돌리니까 통과.. 근데 뭔가 다른 방법이 없을까 하는 생각,, 아쉬움이 남는다..
N = int(input())
cnt = 0
while N > 0:
    n = map(int, list(str(N)))
    if N%sum(n) == 0:
        cnt += 1
    N -= 1
print(cnt)
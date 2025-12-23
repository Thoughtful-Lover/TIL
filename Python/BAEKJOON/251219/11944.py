# N과 M을 각각 입력 받음
N, M = map(int, input().split())
# N을 N번 출력하는 경우와 M자리만큼 출력하는 경우 중 더 작은 값을 변수 length에 저장
length = min(N*N, M)
# N을 문자열 형태로 바꾸고, 출력할 길이를 N으로 나눈 몫보다 1만큼 크게 만들되, 전체 길이는 length를 넘지 않도록 함
# 이는 M자리수가 N값의 반복의 중간에서 멈출 경우를 대비하는 것임
print((str(N)*N)[:length])
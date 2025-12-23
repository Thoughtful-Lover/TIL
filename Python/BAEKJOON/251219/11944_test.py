# N과 M을 각각 입력 받음
N, M = map(int, input().split())
# N을 N번 출력하는 경우와 M자리만큼 출력하는 경우 중 더 작은 값을 변수 length에 저장
length = min(N*N, M)
# 추후 처리를 위해 N을 문자열로 바꿔주고
N = str(N)
# 출력할 길이를 N의 길이로 나눈 몫보다 1만큼 크게 만들되, 전체 길이는 length를 넘지 않도록 함
# 이는 M자리수 만큼 출력할 때, N값이 반복되다가 N값의 중간 위치 어딘가에서 출력이 멈추는 경우를 고려함
print((N*(length//len(N)+1))[:length])
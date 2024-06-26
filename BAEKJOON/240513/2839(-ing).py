'''
2839. 설탕 배달

3킬로그램 봉지와 5킬로그램 봉지
설탕을 정확하게 N킬로그램 배달해야할 때, 봉지 몇 개를 가져가면 되는지

첫째 줄에 N (3 <= N <= 5000)
정확하게 N킬로그램을 만들 수 없다면 -1
'''


# N값을 입력
N = int(input())
# 설탕의 최소 운반 개수를 저장할 변수 min_num
# 만약 운반할 수 없는 경우 -1을 출력해야 하므로 초기 값은 -1
min_num = -1
# 5kg 설탕의 운반량을 저장할 변수 five
five = 0
# 5kg짜리 설탕 봉지를 점차 늘려가면서 계산하려고 함
# Nkg을 넘을 때까지 시행
while N > five:
    # 만약 5kg짜리를 빼고 남은 값이 3으로 나누어 떨어지면
    if (N-five)%3 == 0:
        # 5킬로 짜리 봉지 개수와, 전체 값에서 5킬로짜리 무게를 뺀 값(3kg짜리 봉지)의 합이 min_num보다 작거나, min_num 값이 초기 값이면
        if min_num > (five//5+(N-five)//3) or min_num < 0:
            # min_num 값을 갱신
            min_num = (five//5+(N-five)//3)
    # 5킬로 봉지의 무게를 증가시킴
    five += 5
# 반복을 마친 min_num 값을 출력
print(min_num)
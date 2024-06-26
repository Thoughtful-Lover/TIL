'''
17362. 수학은 체육과목 입니다 2

엄지 1, 검지 2, 중지 3, 약지 4, 소지 5,
약지 6, 중지 7, 검지 8, 엄지 9 의 순서로 수를 센다.

세어야 하는 수 N이 주어지면,
해당수가 해당하는 손가락의 번호 (엄지 1, 검지 2, 중지 3, 약지 4, 소지 5) 를 출력하시오.
'''

# 목표인 숫자 N을 입력 받고
N = int(input())
# 맨 앞 다섯 개의 수를 처리하기 위해 5를 뺀 값을 N_a로 저장
N_a = N-5
# 5까지 숫자를 세고 그 이후로는 4개씩 단위를 끊어서 숫자를 세기 위해 N_b를 만듬
N_b = N_a//4
# N_c 값으로 검지부터 셌을 때 몇 번째인지를 셀 수 있음
N_c = N_a%4
# 5를 뺀 값이 0보다 크지 않으면 처음 다섯 개의 수이므로 그대로 출력
if N_a <= 0:
    print(N)
# 그 다음부터 0을 포함한 짝수 번에는 수가 역순으로 올라감 그래서 N_b가 짝수일 때는 수를 셀 때 약지부터 세는걸 가정
elif N_b%2 == 0:
    # 즉, 약지부터 셌을 때 N_c가 1,2,3,4 이런 식으로 수가 매겨지므로 실제 손가락의 번호는 5-N_c가 된다.
    print(5-N_c)
# 홀수 번에는 수가 정순으로 올라감. 이때는 수를 검지부터 세는걸 가정
else:
    # 검지부터 셌을 때, 1,2,3,4 이런 식으로 수가 매겨지므로 실제 손가락의 번호는 N_c+1이 된다.
    print(N_c+1)

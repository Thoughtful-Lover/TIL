'''
10953. A+B - 6

두 정수 A와 B를 입력받은 다음 A+B를 출력

첫째 줄에 테스트 케이스 개수 T
각 테스트 케이스는 한 줄, A와 B는 콤마로 구분 (0<A,B<10)
'''

T = int(input())
# 테스트 케이스 별 시
for _ in range(T):
    # 주어진 테스트 케이스를 리스트로 입력 받고
    A_and_B = list(input())
    # 인덱스 1에 있는 ,를 제외한 첫 번째, 세 번째 값을 수로 바꾸어 더해서 출력
    print(int(A_and_B[0])+int(A_and_B[2]))
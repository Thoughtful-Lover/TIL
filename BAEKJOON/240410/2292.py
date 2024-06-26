'''
2292. 벌집

벌집의 규칙을 찾는다.
1: 6^0
2: 6^0 + 6^1
3: 6^0 + 6^1 + 6^2
'''


'''
벌집의 규칙을 찾는다.
출발점: 1
출발점과 1칸으로 연결되어 있음: 1 + 6*1
출발점과 2칸으로 연결되어 있음: 1 + 6*1 + 6*2
...
'''

# 수를 입력 받음
N = int(input())
# 6의 배수의 합으로 번호가 결정되므로, 곱하여 6의 배수를 만들어 줄 변수 i
i = 0
# 지금까지의 벌집 방의 번호를 저장할 변수 sum_num
sum_num = 1
while True:
    # 값을 갱신해주면서
    sum_num += 6*i
    i += 1
    # 만약에 N이 sum_num보다 작을 때, 지나간 방의 개수를 프린트 해줄 수 있다.
    if N <= sum_num:
        print(i)
        break

'''
13752. 히스토그램

첫 번째 줄에는 테스트 케이스의 개수 n (1 ≤ n ≤ 100)이 주어진다. 다음 n 개의 줄에는 각 히스토그램의 크기 k (1 ≤ k ≤ 80)가 주어진다.
각 테스트 케이스에 대해서 히스토그램의 크기 k와 동일한 수의 '='를 출력한다. '='사이에 공백은 존재하지 않는다.
'''

# 테스트 케이스 수 n을 입력 받음
n = int(input())
# n번의 테스트 케이스를 수행
for _ in range(n):
    # 히스토그램의 크기 k를 입력 받고
    k = int(input())
    # 한 줄에 나란히 k 크기의 히스토그램을 출력
    for _ in range(k):
        print('=', end='')
    # 한 칸 띄운 값으로 출력
    print()
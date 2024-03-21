'''
2566. 최댓값

9*9 2차원 배열
최댓값과
몇 행 몇 열에 위치한지 출력

최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
'''

# 2차원 배열을 입력 받고
matrix = [list(map(int, input().split())) for _ in range(9)]
# 최대값과, 행 번호, 열 번호를 저장할 리스트 max_value 를 정의
max_value = [-1] * 3

for i in range(9):
    for j in range(9):
        # max_value에 기존에 저장된 값이 탐색한 값보다 작으면
        # 단, 문제 조건 때문에 등호를 포함해도 무관
        if max_value[0] < matrix[i][j]:
            max_value[0] = matrix[i][j]
            # 탐색은 인덱스로 접근하는데 행과 열 번호는 1번부터 시작하므로 +1하여 저장
            max_value[1] = i+1
            max_value[2] = j+1

print(max_value[0])
print(max_value[1], max_value[2])
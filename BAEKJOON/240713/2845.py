'''
2845. 파티가 끝나고 난 뒤

상근이는 1m^2당 몇 명의 사람이 자기 파티에 있었는지 알고 있다.
서로 다른 5개의 신문을 보면서 기사에 적혀 있는 참가자 수가 실제랑 얼마나 다른지 구하려고 한다.
'''


# 빠른 입력을 위해 sys를 import
import sys

# 1m^2당 사람의 수 L 과 파티가 열렸던 곳의 넓이 P 를 각각 입력 받음
L, P = map(int, sys.stdin.readline().split())
# 신문에서 보도한 참가자 수의 정보를 배열 newspapers에 저장
newspapers = list(map(int, sys.stdin.readline().split()))
# 파티에 참가한 수를 구하여 변수 people에 저장
people = L*P
# 배열을 순회하며 뉴스에서 보도된 참가자 수에서 실제 참여자수의 값을 빼주고 출력해준다.
for newspaper in newspapers:
    print(newspaper-people, end=' ')
print()
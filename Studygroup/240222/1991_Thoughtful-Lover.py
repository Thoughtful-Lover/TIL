'''
1991. 트리 순회

이진 트리를 입력 받아, 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램을 작성

첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
자식 노드가 없는 경우에는 .으로 표현
'''


def preorder(n):
    while True:
        print(tv[n], end='')
        preorder(tv.index(left[n]))
        preorder(tv.index(right[n]))

# def inorder(n):
# def postorder(n):

import sys

N = int(sys.stdin.readline())
left = [0] * (N+1)
right = [0] * (N+1)
tv = [0] * (N+1)

for i in range(1, N+1):
    info = list(sys.stdin.readline())
    info.remove('.')

    tv[i] = info[0]
    if len(info) >= 2:
        left[i] = info[1]
    if len(info) == 3:
        right[i] = info[2]

preorder(1)
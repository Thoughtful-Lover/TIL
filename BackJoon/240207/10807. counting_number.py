'''
108097. 개수 세기

문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다.
셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
'''

N = int(input())
arr = list(map(int, input().split()))
v = int(input())

count = 0       # v 의 개수를 셀 변수 count 를 정의

for num in arr:     # 입력 받은 수의 리스트를 순회하며 v 와 같은 수가 있을 경우 count 를 1 증가
    if num == v:
        count += 1

print(count)

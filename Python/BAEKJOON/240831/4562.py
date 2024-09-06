'''
4562. No Brainer

첫 번째 줄에 데이터 셋의 개수
그 다음부터 한줄에 좀비가 먹는 뇌의 개수 X와 좀비가 살아남기 위한 뇌의 개수 Y 가 나란히 입력
X가 Y보다 크거나 같으면 "MMM BRAINS"를
아니면 "NO BRAINS"를 출력
'''

n = int(input())
for _ in range(n):
    X, Y = map(int, input().split())
    if X >= Y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")
'''
27930. 당신은 운명을 믿나요?

앞에서부터 순서대로 문자를 읽어갈 때 먼저 YONSEI나 KOREA를 찾을 수 있으면 해당 학교에 합격함
두 학교에 동시에 합격하는 경우는 없다.
'''

from collections import deque


# 문자를 입력 받고
chars = deque(input())
# 연세대와 고려대의 낱말에 해당하는 데크를 작성
y = deque(['Y', 'O', 'N', 'S', 'E', 'I'])
k = deque(['K', 'O', 'R', 'E', 'A'])
while True:
    # 연세대의 문자가 먼저 비게 되면
    # yonsei를 출력하고 반복문 종료
    if not y:
        print('YONSEI')
        break
    # 고래대의 문자가 먼저 비게 되면
    # korea를 출력하고 반복문 종료
    elif not k:
        print('KOREA')
        break
    # 입력 받은 문자의 첫 번째를 하나 뽑아서
    char = chars.popleft()
    # yonsei와 korea 중 해당하는 문자가 있으면 문자를 제거한다.
    if y[0] == char:
        y.popleft()
    if k[0] == char:
        k.popleft()
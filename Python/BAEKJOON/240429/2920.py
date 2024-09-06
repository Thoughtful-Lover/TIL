'''
2920. 음계

1부터 8까지 차례대로 연주한다면 ascending,
8부터 1까지 차례대로 연주한다면 descending,
둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
'''

# 연주한 순서를 저장한 리스트 play
play = list(map(int, input().split()))
# 해당 연주를 오름차순으로 정리한 asc
asc = sorted(play)
# 해당 연주를 내림차순으로 정리한 desc
desc = sorted(play, reverse=True)

# 만약 연주가 오름차순으로 정리한 asc와 같다면, 이 연주는 ascending
if play == asc:
    print('ascending')
# 만약 연주가 내림차순으로 정리한 desc와 같다면, 이 연주는 descending
elif play == desc:
    print('descending')
# 그 이외의 경우는 mixed
else:
    print('mixed')


# 앞뒤의 음을 일일이 계산하여 여부를 구하는 방식
'''# 연주한 순서를 저장한 리스트 play
play = list(map(int, input().split()))
# 음이 증가했는지 여부를 표시할 변수 asc 와 감소했는지 여부를 표시할 변수 desc
asc = 0
desc = 0
# 이전에 연주한 음을 저장할 변수 prev
prev = 0

# 연주한 순서를 순회함
for hmm in play:
    # 이전 값이 0이면 첫 연주이기 때문에 prev에 현재 값을 저장하고 continue
    if prev == 0:
        prev = hmm
        continue
    # 현재음이 이전 음보다 높으면 asc를 1로 바꿔줌
    if hmm > prev:
        asc = 1
    # 현재음이 이전 음보다 낮으면 desc를 1로 바꿔줌
    elif hmm < prev:
        desc = 1
    # prev를 현재값으로 갱신
    prev = hmm

# asc와 desc가 모두 1이면, 증가 구간과 감소 구간이 모두 포함되어 있으므로 mixed를 출력
if asc == 1 and desc == 1:
    print('mixed')
# asc만 1이면 ascending을 출력
elif asc == 1:
    print('ascending')
# 나머지는 descending을 출력
else:
    print('descending')'''


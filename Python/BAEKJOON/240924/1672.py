'''
1672. DNA 해독

N개의 A,G,C,T로 구성된 DNA염기셔열
'''

# deque를 import
from collections import deque

# 염기서열 쌍의 조합을 딕셔너리로 만듬
graph = {
    'AA': 'A',
    'AG': 'C',
    'AC': 'A',
    'AT': 'G',
    'GA': 'C',
    'GG': 'G',
    'GC': 'T',
    'GT': 'A',
    'CA': 'A',
    'CG': 'T',
    'CC': 'C',
    'CT': 'G',
    'TA': 'G',
    'TG': 'A',
    'TC': 'G',
    'TT': 'T'
}

# N을 입력 받고
N = int(input())
# 염기 서열의 값들을 deque로 입력 받음
bs = deque(list(input()))
# 값이 하나만 남을 때까지 시행
while len(bs) > 1:
    # 앞뒤 순서가 중요한게 아니므로 그냥 뒤의 2개 값을 뽑아서 pair에 저장해주고
    pair = bs.pop()
    pair += bs.pop()
    # graph를 참고해서 새로운 값을 제일 오른쪽에 넣어주는 식으로 반복
    bs.append(graph[pair])
# 리스트 값을 간편하게 출력
print(*bs)
# 문제 이해
### 5525. IOIOI
* N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
  * P1 IOI 
  * P2 IOIOI 
  * P3 IOIOIOI 
  * PN IOIOI...OI (O가 N개)
* I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S 안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
### 입력
* 첫째 줄 N
* 둘째 줄 S의 길이 M
* 셋째 줄 S
### 출력
S에 PN이 몇 군데 포함되어 있는지를 출력
### 제한
* 1<=N<=1,000,000
* 2N+1<=M<=1,000,000
* S는 I와 O로만 이루어져 있다.
# 문제 설계
* 그냥 문자열 슬라이싱으로 다 확인해보면될 것 같은데?
* 시간이 얼마나 걸릴지 확신이 없긴 하다..
# 문제 풀이
### 1차 시도
```python
# N, M을 입력 받고, S는 문자열로 입력 받음
N = int(input())
M = int(input())
S = input()
# N+1개의 I와 N개의 O로 이루어진 수 N
PN = 'IO'*N+'I'
# 문자열 S에 PN이 포함되는 위치를 저장할 변수 cnt
cnt = 0
# 문자열 위를 문자열의 시작점을 인덱스의 시작점으로 하므로, 전체 길이에서 PN만큼의 길이를 뺀다.
for i in range(M-N*2):
    # PN의 길이만큼 슬라이싱 한 값이 PN과 같으면
    if S[i:i+N*2+1] == PN:
        # cnt를 1 증가
        cnt += 1
# 위 반복이 종료되면 cnt를 출력
print(cnt)
```
* 절반은 맞았는데 절반은 틀림
* S의 길이가 길어지니까 시간 초과
* 아 맞다 ```count()``` !!!
### 2차 시도
```python
# N, M을 입력 받고, S는 문자열로 입력 받음
N = int(input())
M = int(input())
S = input()
# N+1개의 I와 N개의 O로 이루어진 수 N
PN = 'IO'*N+'I'
# count 함수를 활용해 S에 포함된 PN의 개수를 출력
print(S.count(PN))
```
* 아니 근데 이거 중첩되는 문자열이 탐색이 안돼..
* find 함수 써볼게요...
### 3차 시도
```python
N = int(input())
M = int(input())
S = input()
# N+1개의 I와 N개의 O로 이루어진 수 N
PN = 'IO'*N+'I'
# 문자열 S에 PN이 포함되는 위치의 개수를 저장할 변수 cnt
cnt = 0
# 탐색의 시작 위치 0
start = 0
# 반복
while True:
    # 시작점을 start로 할 때, 처음으로 등장하는 PN과 동일한 문자열의 위치를 location에 저장
    location = S.find(PN, start)
    # 만약 이 값이 존재하지 않으면 반복 종료
    if location == -1:
        break
    # 존재하면 cnt를 1 증가하고 다음 탐색 위치를 현재 문자열 위치 바로 뒤부터로 넘김
    else:
        cnt += 1
        start = location+1
print(cnt)
```
* 또간 초과....
### 4차 시도
```python
import re

N = int(input())
M = int(input())
S = input()
# N+1개의 I와 N개의 O로 이루어진 수 N
PN = 'IO'*N+'I'

print(re.findall(PN, S))
```
* 이것도 중첩되는 문자열을 못 찾는다...
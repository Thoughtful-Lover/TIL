'''
10814. 나이순 정렬

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''

N = int(input())
# 가입한 사람들의 정보를 저장해줄 리스트 members 를 정의
members = [0] * N
# 가입한 사람들의 정보를 리스트에 차례로 입력
for i in range(N):
    member = list(input().split())
    members[i] = member
# 나이를 오름차순으로 해서 리스트를 정렬
# 이거를 int로 처리하고 안하고 차이가 있을까?
members.sort(key=lambda x: int(x[0]))

# 가입한 사람들의 정보를 한 줄씩 출력
for member_info in members:
    print(*member_info)
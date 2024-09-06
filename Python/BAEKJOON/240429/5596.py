'''
5596. 시험 점수

민국이와 만세는 4과목(정보, 수학, 과학, 영어)에 대한 시험을 봤다.
민국이와 만세가 본 4과목의 점수를 입력하면, 민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력하는 프로그램을 작성하시오.
단, 서로 동점일 때는 민국이의 총점 S를 출력한다.
'''

# 민국이와 만세의 점수를 각각 리스트 mignuk 과 manse 로 입력 받음
minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))

# 변수 S,T에 각각 minguk과 manse의 총점을 저장
S = sum(minguk)
T = sum(manse)

# S가 T보다 크거나 같으면 S를 출력
if S >= T:
    print(S)
# T가 더 크면 T를 출력
else:
    print(T)
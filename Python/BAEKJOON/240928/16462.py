'''
16462. '나교수' 교수님의 악필

악필이라 구분이 되지 않는 교수님의 0, 6, 9를 그냥 9로 통일하기로 함
평균 성적과 가장 가까운 수를 출력
'''

# 전체 점수의 개수를 입력 받고
N = int(input())
# 총점을 저장할 변수 score
score = 0
for _ in range(N):
    # 수를 입력 받음
    num = int(input())
    # 입력 받은 수가 100점이면 100을 더해줌
    if num == 100:
        score += 100
        continue

    # 십의 자리 수가 6인 경우 90을 더해 주고, 그게 아닌 다른 수들은 원래 수대로 더해줌
    if num//10 == 6:
        score += 90
    else:
        score += (num//10)*10

    # 일의 자리 수가 6이나 0인 경우, 9를 더해 주고, 그게 아닌 다른 수들은 원래 수대로 더해줌
    if num%10 == 6 or num%10 == 0:
        score += 9
    else:
        score += num%10

# 계산한 결과값의 소수점 뒷자리 수를 반올림 처리해줌
if (score/N)%1 >= 0.5:
    print(int((score/N)//1+1))
else:
    print(int((score/N)//1))
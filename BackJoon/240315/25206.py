'''
25206. 너의 평점ㅂ은

치훈이의 전공 평점을 계산해주는 프로그램
전공평점은 전공과목별 (학점*과목평점)의 합을 학점의 총합으로 나눈 값
'''

# 문제에서 주어진 학점을 딕셔너리로 만듬
grade_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

# 총 학점수를 더할 cnt와 총 평점을 더할 grade_sum
cnt = 0
grade_sum = 0

while True:
    try:
        name, credit, grade = input().split()
        # P/F 과목은 넘어간다
        if grade == 'P' or grade == 'F':
            continue
        # 문제에 주어진 조건대로 (학점*과목평점)의 합을 학점의 총합으 나누고자 한다.
        grade_sum += grade_dict[grade] * float(credit)
        cnt += float(credit)
    except:
        break

# 만약 all F일 경우 ZeroDivisionError가 발생하므로 이 조건을 반영한다.
if grade_sum > 0:
    print(grade_sum/cnt)

else:
    print(0)


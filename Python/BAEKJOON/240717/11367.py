'''
11367. Report Card Time

n개의 이름과 점수를 입력 받으면 주어진 점수에 따라 이름과 성적을 출력한다.
A+: 97-100
A: 90-96
B+: 87-89
B: 80-86
C+: 77-79
C: 70-76
D+: 67-69
D: 60-66
F: 0-59
'''


# n을 입력 받고
n = int(input())
# n명의 이름과 점수를 입력 받고, 조건에 맞게 grade로 바꾸어 출력해준다.
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score >= 97:
        score = 'A+'
    elif 90 <= score <= 96:
        score = 'A'
    elif 87 <= score <= 89:
        score = 'B+'
    elif 80 <= score <= 86:
        score = 'B'
    elif 77 <= score <= 79:
        score = 'C+'
    elif 70 <= score <= 76:
        score = 'C'
    elif 67 <= score <= 69:
        score = 'D+'
    elif 60 <= score <= 66:
        score = 'D'
    elif score <= 59:
        score = 'F'
    print(name, score)
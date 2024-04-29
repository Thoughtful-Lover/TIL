'''
27889. 특별한 학교 이름

NLCS: North London Collegiate School
BHA: Branksome Hall Asia
KIS: Korea International School
SJA: St. Johnsbury Academy

각 학교의 약칭이 주어졌을 때, 정식 명칭을 출력하는 프로그램을 작성하시오.
'''

# 학교의 약칭을 키로, 정식 명칭을 value로 가지는 딕셔너리 special_school_name 을 정의
special_school_name = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}

# 학교의 약칭을 입력하면, 이 값을 키로 하는 학교의 정식 명칭을 딕셔너리에서 출력
school = input()
print(special_school_name[school])
'''
10172. 개

아래 예제와 같이 개를 출력하시오.

|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\ ')
print('|"^"`    |')
print('||_/=', end='')
# '\' 이 부호에서 자꾸 오류가 떠서 아래와 같은 방법으로 출력
a = '\ '
a = a.rstrip()
print(a, end='')
print('\__|')
'''
14581. 팬들에게 둘러싸인 홍준

선풍기 모양의 이모티콘은 :fan: 이고, 홍준의 이모티콘은 :(홍준의 아이디): 이다.
홍준의 아이디가 주어지면 구사과가 만든 이모티콘을 출력하는 프로그램을 작성하여라.
자세한 출력 방식은 입출력 형식을 참고하면 된다.

예제 입력
appa

예제 출력
:fan::fan::fan:
:fan::appa::fan:
:fan::fan::fan:
'''

# 홍준이의 아이디를 입력 받고
hongjun_id = input()
# f-string으로 값을 출력해준다.
print(':fan::fan::fan:')
print(f':fan::{hongjun_id}::fan:')
print(':fan::fan::fan:')
'''
25915. 연세여 사랑한다.

비밀번호 ILOVEYONSEI
현재 위치가 입력으로 주어질 때
이동해서 비밀번호를 입력할 수 있는 최소 이동수는
알파벳 한 칸당 1번 이동
'''

# 처음 시작점이 I인 경우의 최소 이동수는 84
# 따라서 처음 입장 위치에서 I까지의 이동하는 거리에 위의 값을 더해주면 된다.
c = input()
# 유니코드 정수 값의 차를 통해 두 알파벳 간 거리를 구해준다.
print(84+abs(ord(c)-ord('I')))
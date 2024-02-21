'''
2744. 대소문자 바꾸기

영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
'''


import sys

string = sys.stdin.readline()
# 대소문자를 바꿔주는 swapcase 메서드를 이용
string = string.swapcase()
print(string)
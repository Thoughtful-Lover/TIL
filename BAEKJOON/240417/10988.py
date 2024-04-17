'''
10988. 팰린드롬인지 확인하기

앞으로 읽을 때와 뒤로 읽을 때가 똑같은 단어를 팰린드롬
단어를 입력 받고
단어가 팰린드롬이면 1, 아니면 0을 출력
'''


# 문자열 리스트가 팰린드롬인지 계산해주는 함수 is_palindrome을 정의
def is_palindrome(string_list, string_length):
    # 양 끝에서 동시에 출발해서 문자열을 검사
    for i in range(string_length//2):
        # 만약 하나씩 비교할 때 하나라도 다른 문자가 나온다면 0을 반환
        if string_list[i] != string_list[-(i+1)]:
            return 0
    # 위의 반복문을 무사히 넘기면 1을 반환
    return 1


# 문자열을 리스트로 입력 받아, my_string에 할당
my_string = list(input())
# 리스트의 길이를 계산해서 변수 length에 할당
length = len(my_string)
# 함수에 위에서 구한 두 값을 입력하여 그 반환값을 출력하려고 함
print(is_palindrome(my_string, length))
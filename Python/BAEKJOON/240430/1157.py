'''
1157. 단어 공부

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는
프로그램
'''

# 알파벳들 개수 만큼의 요소를 가지는 리스트 alphabets 이곳에 각 철자의 개수를 저장해주낟.
alphabets = [0]*26
# 아스키 코드를 이용할 계획! 알파벳 소문자와 대문자의 아스키 코드 값을 파악해 둔다.
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90

# 단어를 리스트로 입력 받는다.
word = list(input())

# 단어를 순회하며
for alph in word:
    # 철자를 아스키 코드 값으로 바꿔준다.
    alph = ord(alph)
    # 소문자일 경우 97만큼 뺀 값이 해당 알파벳을 나타내는 인덱스 값이고
    if alph > 90:
        alphabets[alph-97] += 1
    # 대문자일 경우 65만큼 뺀 값이 해당 알파벳을 나타내는 인덱스 값이다.
    elif alph < 91:
        alphabets[alph-65] += 1

# 개수를 모두 센 후, 개수의 최대 값을 변수 max_v에 저장
max_v = max(alphabets)
# 그리고 해당 인덱스 값을 변수 max_indx에 저장
max_idx = alphabets.index(max_v)
# 해당 최대값을 초기화해주고
alphabets[max_idx] = 0
# 만약 해당 최대값을 지웠는데도 같은 최대값이 존재한다면 최대값이 여러개이므로 '?'를 출력
if max_v == max(alphabets):
    print('?')
# 그게 아니라면, 해당 알파벳을 대문자로 출력해야하므로, 조금 전 구한 인덱스 값에 65를 더해 문자열로 다시 출력
else:
    print(chr(max_idx+65))
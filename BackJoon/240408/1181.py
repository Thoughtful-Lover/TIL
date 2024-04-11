'''
1181. 단어 정렬

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
'''

# 입력받음
N = int(input())
# N개의 단어를 저장할 리스트 alphabet_list를 정의
alphabet_list = [0] * N
# 리스트에 차곡차곡 입력 받음
for i in range(N):
    word = input()
    alphabet_list[i] = word
# 먼저 길이를 기준으로, 길이가 같으면 알파벳순(오름차순)으로 정렬
alphabet_list.sort(key=lambda x: (len(x), x))
# 이전 값을 저장해줄 변수 previous
previous = ''
# 리스트를 순회하며 이전에 있던 값과 같지 않은 값만 출력해줌 (중복을 피함)
for the_word in alphabet_list:
    if the_word != previous:
        print(the_word)
    previous = the_word
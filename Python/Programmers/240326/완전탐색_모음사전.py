'''
사전에 알파벳모음 A, E, I, O, U만 만들어서 사용할 수 있는 길이 5 이하의 단어
A / AA / ... / UUUUU

조합,
'''

'''
이렇게 하면 이 문제는
1, 2, 3, 4, 5 중 숫자를 뽑아서 수를 만들고 뒤에 0을 붙여서 순서를 만드는 문
'''

alphabet = {
    'A': 1,
    'E': 2,
    'I': 3,
    'O': 4,
    'U': 5
}
cnt = 0

word_list = list(word)
for i in range(5):
    if i >= len(word_list):
        break
    word_list[i] = alphabet[word_list[i]]
word_string = ''
for num in word_list:
    word_string += str(num)


def dictionary(word, compare, time):
    global cnt

    if time == 6:
        return

    for j in range(1, 6):
        new_compare = compare + str(j)
        cnt += 1
        if word == new_compare:
            answer = cnt
            print(answer)
            return
        dictionary(word, new_compare, time+1)


dictionary(word_string, '', 1)
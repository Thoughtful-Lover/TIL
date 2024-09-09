# 전체 문서를 리스트로 입력 받고
document = list(input())
# 검색하려는 단어도 리스트로 입력 받는다
word = list(input())
# 문서의 길이를 변수 docu_length에
docu_length = len(document)
# 검색하려는 단어의 길이를 변수 word_length에 저장
word_length = len(word)
# 현재 탐색하고 있는 문서의 인덱스 값을 저장해줄 변수 current
current = 0
# 검색하는 단어의 개수를 저장할 변수 cnt
cnt = 0
# 현재 위치를 첫 번째 철자로 하고 검색하려는 단어만큼의 길이를 가질 때 이 단어의 인덱스 값이 문서 전체의 인덱스 값을 벗어나지 않는다면 계속 시행
while docu_length-1 >= current+word_length-1:
    # 문서를 검색하던 중 검색하려는 단어가 아니기 때문에, 멈추었는지 여부를 저장할 변수 is_break
    is_break = False
    # 단어의 길이만큼 시행
    for i in range(word_length):
        # 만약 현재 위치에서의 알파벳 값과 단어에서의 알파벳 값이 다르다면
        if document[current+i] != word[i]:
            # is_break 를 True로 바꿔주고
            is_break = True
            # 현재 위치를 갱신. 보수적으로 계산해서 다음 값부터는 맞을 수도 있잖아? 그래서 +1
            current += 1
            break
    # 만약 단어를 하나 온전히 찾았다면
    if not is_break:
        # 개수를 1 증가시켜 주고
        cnt += 1
        # 현재 위치를 단어 하나의 개수만큼 갱신
        current += word_length
# 위 반복문이 끝나면 cnt를 출력
print(cnt)

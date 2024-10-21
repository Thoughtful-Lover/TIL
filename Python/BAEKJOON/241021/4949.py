while True:
    sentence = list(input())
    if len(sentence) == 1:
        break
    stack = []
    is_stopped = False
    for word in sentence:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')' or word == ']':
            if stack and ((word == ')' and stack[-1] == '(') or (word == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                print('no')
                is_stopped = True
                break
    if is_stopped:
        continue
    print('yes')
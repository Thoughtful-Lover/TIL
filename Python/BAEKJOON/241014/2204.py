while True:
    n = int(input())
    if not n:
        break
    words = [0]*n
    words_modified = [0]*n
    for i in range(n):
        word = input()
        words[i] = word
        words_modified[i] = (word.lower(), i)
    words_modified.sort(key=lambda x: x[0])
    print(words[words_modified[0][1]])
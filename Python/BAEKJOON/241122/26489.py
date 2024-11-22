cnt = 0
while True:
    try:
        the_sentence = input()
        if the_sentence ==  'gum gum for jay jay':
            cnt += 1
    except:
        break
print(cnt)
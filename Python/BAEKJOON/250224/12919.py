def add_a(string):
    string += 'A'
    return string


def add_b(string):
    string += 'B'
    string = string[::-1]
    return string


def check_string(string):
    global answer
    if answer:
        return
    if string == T:
        answer = 1
        return
    elif len(string) >= len(T):
        return
    check_string(add_a(string))
    check_string(add_b(string))


answer = 0
S = input()
T = input()
check_string(S)
print(answer)
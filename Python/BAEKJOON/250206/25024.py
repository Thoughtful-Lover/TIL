def is_time(a, b):
    if a<=23 and b<=59:
        return 'Yes'
    return 'No'


def is_date(a, b):
    if 1<=a<=12 and 1<=b<=31:
        if a in (1, 3, 5, 7, 8, 10, 12) or (a in (4, 6, 9, 11) and b<=30) or b<=20:
            return 'Yes'
    return 'No'

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(is_time(x, y), is_date(x, y))
# for i in range(2, 17, 2):
#     print(i)

def is_number_valid(card_numbers: list):
    for i in range(2, 17, 2):
        num = card_numbers[-i]*2
        if num>=10:
            num = num//10+num%10
        card_numbers[-i] = num
    if sum(card_numbers)%10:
        return 'F'
    else:
        return 'T'


T = int(input())
for _ in range(T):
    numbers = list(map(int, input()))
    print(is_number_valid(numbers))
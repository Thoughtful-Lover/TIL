'''
17284. Vending Machine

어머니께 5000원
1을 누르면 500원 레쓰비
2를 누르면 800원 게토레이
3을 누르면 1000원 코카콜라

거스름돈을 출력
'''

# 초기 용돈 5000원
money = 5000
# 누른 버튼값을 리스트로 입력 받음
order = list(map(int, input().split()))
# 리스트를 순회하며
for drink in order:
    # 각각의 수에 따른 음료 가격을 원래 받은 돈에서 빼준다.
    if drink == 1:
        money -= 500
    elif drink == 2:
        money -= 800
    elif drink == 3:
        money -= 1000
# 반복문이 끝나면 남은 돈의 액수를 출력
print(money)
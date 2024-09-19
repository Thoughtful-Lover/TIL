N = int(input())
cardsPrice = list(map(int, input().split()))
price = 0
for i in range(N):
    cardsPrice[i] = (i+1, cardsPrice[i]/(i+1))
cardsPrice.sort(key=lambda x:x[1], reverse=True)
print(cardsPrice)
while N > 0:
    for card in cardsPrice:
        if N >= card[0]:
            N -= card[0]
            price += int(card[0]*card[1])
            break
print(price)
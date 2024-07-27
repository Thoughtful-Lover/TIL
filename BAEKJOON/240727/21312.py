'''
21312. 홀짝 칵테일

정진이는 정수로 부여된 고유한 수를 가지는 음료를 섞어 칵테일을 만든다.
맛이 홀수인 칵테일이 짝수인 칵테일보다 무조건 맛있고
같은 홀수, 짝수끼리 중에서는 수가 무조건 클수록 맛있다.

세 음료가 주어질 때 가장 맛있는 칵테일 맛을 출력
첫째 줄에는 주어진 세 음료의 고유번호 A, B, C가 주어진다.
1 ≤ A, B, C ≤ 100
'''


# 문제를 이해해보면, 홀수가 하나라도 포함되면 홀수끼리의 곱을 출력하고,
# 홀수가 하나도 없다면 짝수끼리의 곱 (세수의 곱)을 출력하면 된다.

# 3개의 음료수의 정수를 리스트로 입력 받는다.
drinks = list(map(int, input().split()))
# 홀수 칵테일과 짝수 칵테일을 변수로 설정해주고 초기값을 각각 0으로 해준다.
odd_cocktail, even_cocktail = 0, 0
# 리스트를 순회하며 홀수이면 odd_cocktail에 곱하고, 짝수면 even_cocktail에 곱한다.
for drink in drinks:
    if drink%2:
        # 각각의 칵테일의 값이 0이라면 칵테일 값을 음료의 값으로 바꿔준다.
        if not odd_cocktail:
            odd_cocktail = drink
            continue
        odd_cocktail *= drink
    else:
        if not even_cocktail:
            even_cocktail = drink
            continue
        even_cocktail *= drink
# 리스트 순회를 마친 후, 만약에 홀수 칵테일에 변동이 없다면 짝수 칵테일을 출력하고
if not odd_cocktail:
    print(even_cocktail)
# 그게 아니면 홀수 칵테일을 출력한다.
else:
    print(odd_cocktail)

'''
처음에 odd_cocktail과 even_cocktail 의 초기값을 각각 1, 1로 하고
odd_cocktail 값이 1일 때 짝수 칵테일을 출력하는 쪽으로 했는데
A = B = C = 1 인 경우가 있어서 틀렸다.
따라서 위와 같이 코드를 수정하였다.
'''
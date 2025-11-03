# 경쟁사 제품 가격 A, 경쟁사 제품 성능 B, WARBOY의 가격 C
A, B, C = map(int, input().split())
# WARBOY의 성능을 X라고 하면,
# 경쟁사 제품의 가격 대비 성능 B/A, WARBOY의 가격 대비 성능 3*(B/A)= X/C
# 따라서, X = 3*(B/A)*C
print(3*(B/A)*C)
'''
15829. Hashing

문제 조건을 잘 보자
결과 값을 Mod 인 1234567891 로 나눈 나머지를 출력한다.
'''

N = int(input())
hash_list = list(input())
hash_value = 0

# 알파벳이 몇 번째 순서인지에 31을 인덱스 만큼 제곱한 수를 곱해서 더해주는 문제인 것 같다.
for i in range(N):
    hash_value += (ord(hash_list[i])-96) * (31**i)

print(hash_value%1234567891)
'''
첫 줄에 주어지는 숫자의 개수 N
둘째 줄에 N개의 숫자가 공백 없이 주어짐
'''


N = int(input())
nums = input()      # 숫자를 string 으로 입력 받음

sum = 0
for i in nums:
    sum += int(i)       # 스트링을 순회하면서 sum 에 int 로 변환하여 더해줌

print(sum)
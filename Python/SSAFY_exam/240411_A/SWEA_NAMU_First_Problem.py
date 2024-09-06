# SWEA 나무 높이
# 실제 당일 첫 번째 기출 문제

def tree_grow(num, target):
    cnt = 0
    for i in range(num-1):
        cnt += (target-trees[i])//3*2
        trees[i] = (target-trees[i])%3
    print(trees)
    print(cnt)

    count_one = trees.count(1)
    count_two = trees.count(2)
    if count_one > count_two:
        cnt += count_two*2
        cnt += (count_one-count_two)*2-1
    else:
        # 1일짜리 2개로 2일짜리 물을 줄 수 있는 경우
        cnt += count_one*2
        if (count_two-count_one)%2 == 1:

        else:
        cnt += ()*2
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    print(trees)
    days = tree_grow(N, trees[N-1])
    print(f'#{tc} {days}')
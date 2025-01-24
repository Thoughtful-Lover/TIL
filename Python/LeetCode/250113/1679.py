from collections import Counter

def maxOperations(nums, k):
    answer = 0
    counts = Counter(nums)
    print(counts)
    for key in counts:
        print(key)
        if key * 2 == k:
            answer += key // 2
            print('정답 :', answer)
        elif k - key in counts:
            answer += min(counts[key], counts[k - key])
            counts[key] = 0
            counts[k - key] = 0
    print(answer)
    return answer

maxOperations(nums=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k=2)
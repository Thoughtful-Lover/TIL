'''
문자열을 일정한 단위로 잘라서 중복되는 경우 중복되는 만큼 앞에 숫자를 붙여서 압축할 예정
예) ababababaaaaaacdcddede = 4ab3aa2cd2de
위 문자열을 2 단위로 자르면 다음과 같이 된다.

이러한 규칙에 따를 때 가장 짧은 문자열의 길이를 출력 하시오```
'''
'''
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.
'''

from collections import deque

def solution(s):
    answer = len(s)
    unit = 1
    while unit < len(s)//2+1:
        start = 0
        end = start+unit
        q = deque()
        cnt = 0
        while start < len(s):
            chr = s[start:end]
            start = end
            end = start+unit
            if end > len(s)-1:
                cnt += len(s)-end
            for i in range(len(q)):
                if q[i][1] == chr:
                    q[i][0] += 1
                    break
            q.append([1, chr])
        for i in range(len(q)):
            if q[i][0] > 1:
                cnt += 1
        if answer > unit*len(q)+cnt:
            answer = unit*len(q)+cnt
        unit += 1
    return answer

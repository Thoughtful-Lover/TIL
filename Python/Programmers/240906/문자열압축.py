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

# s = "aabbaccc"


def solution(s):
    # answer의 초기값으로 모든 문자열이 다를 경우 즉, 압축이 하나도 안 될 경우의 크기
    answer = len(s)
    # 압축 단위의 초기값을 1로
    unit = 1
    # 그리고 압축 단위가 문자열의 길이의 1/2일 때까지 시행
    while unit < len(s) // 2 + 1:
        # 시작점은 제일 첫 인덱스
        start = 0
        # 해당 단위의 끝점 인덱스는 start+(단위 길이). 슬라이싱을 활용할거라 마지막 인덱스는 포함되지 않으므로 문제 없다
        end = start + unit
        # 빈 데크를 만들어주고
        q = deque()
        # 문자열의 크기를 저장할 변수 cnt
        cnt = 0
        # 그러면 한 번 해보자. 시작점이 끝 점에 도달하기 전까지를 while 문으로 규정해주고 도중에 break문을 이용해주면 되겠지
        while start < len(s):
            # 단위 크기의 문자열을 슬라이싱 해주고
            chr = s[start:end]
            # 만약 남은 문자열의 크기가 단위 크기보다 작다면 남은 문자열의 길이만큼 더해주고 반복을 종료
            if len(s) - start < unit:
                cnt += len(s) - start
                break
            # q가 차 있는 경우
            if q:
                # 바로 이전에 저장한 값이랑 현재 자른 값이 같다면 값을 추가
                if q[-1][1] == chr:
                    q[-1][0] += 1
                # 그게 아니라면 새로 append
                else:
                    q.append([1, chr])
            # q가 비어 있는 경우 새로 append
            else:
                q.append([1, chr])
            # start 값과 end 값을 갱신
            start = end
            end = start + unit
        # q에 저장된 내용을 탐색해서 앞의 숫자만큼 더해줌
        for i in range(len(q)):
            if q[i][0] > 1:
                # 내가 틀렸던 부분, 처음에는 단순히 cnt += 1 로 했는데 중복되는 문자열의 개수가 10이상일 수 있으므로, 이렇게 해당 숫자의 실제 길이를 더해줘야 함
                cnt += len(str(q[i][0]))
        # 그리고 q에 저장된 문자들과 cnt를 모두 더한 값이 기존 answer보다 작으면 값을 갱신
        if answer > unit * len(q) + cnt:
            answer = unit * len(q) + cnt
        # 단위 크기를 하나 늘려서 반복 계속 돌리기
        unit += 1
    return answer


# print(solution(s))


'''
# 기존 코드
 if q[i][1] == chr:
                    q[i][0] += 1
                    is_there = True
                    break
            if not is_there:
                q.append([1, chr])
'''

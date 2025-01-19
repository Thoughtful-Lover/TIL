def maxVowels(s: str, k: int) -> int:
        vowels = 'aeiou'
        # 답을 저장할 변수 answer
        answer = 0
        # 최초 k 길이 문자열에서 모음의 개수를 저장
        for i in range(k):
            if s[i] in vowels:
                answer += 1
        # 반복적으로 모음의 길이를 저장해 줄 변수 cnt를 정의
        cnt = answer
        print(answer)
        #
        for j in range(len(s)-k+1):
            if s[j] in vowels:
                cnt -= 1
            if s[j+k-1] in vowels:
                cnt += 1
            if answer < cnt:
                answer = cnt
            print(cnt)
        return answer


maxVowels(s='abciiidef', k=3)
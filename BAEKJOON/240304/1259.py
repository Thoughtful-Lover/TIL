'''
1259. 팰린드롬수

거꾸로 뒤집어도 같은 수면 팰린드롬수
팰린드롬수
'''


while True:
    # yes 와 no 출력 여부를 결정하기 위한 변수 done
    done = 0
    N = list(input())
    # 0이 입력되면, 반복문 종료
    if N[0] == '0':
        break
    L = len(N)
    # 절반을 쪼개서 앞뒤를 비교하며 계속 같으면 넘어가고
    for i in range(L//2):
        if N[i] == N[-(1+i)]:
            continue
        # 같지 않은 부분이 있으면 no 를 출력
        print('no')
        done = 1
        break
    # 앞에 no가 출력되지 않았으면 yes를 출력
    if done == 0:
        print('yes')
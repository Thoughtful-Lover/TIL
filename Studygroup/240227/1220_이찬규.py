for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    '''
    while N 번 만큼동안
    충돌할 때까지 위로 올리고 밑으로 내리면
    시간초과 나려나?
    
    '''
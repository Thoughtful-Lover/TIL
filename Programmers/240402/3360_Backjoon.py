'''
3360. 깡총깡총
CTP마을에 사는 토끼 아람이는 3,2,1미터씩 뛰어서 n미터를 지난다.
길이가 주어질 때
점프 길이가 증가하지 않는 순서로 지나가는 방법은
'''


# def ggangchong(target):
#     share = target // 6
#     remain = target%6
#     if remain == 3:
#         return (share*6+1)*3%1000000
#     elif remain == 4:
#         return (share*6+1)*4%1000000
#     elif remain == 5:
#         return (share*6+1)*5%1000000
#     else:
#         return (share*7)%1000000


def ggangchong(num):
    global cnt

    share = num//3
    for i in range(0, share+1):
        cnt += (num-3*i)//2+1


n = int(input())
cnt = 0
ggangchong(n)
cnt = cnt%1000000
print(cnt)

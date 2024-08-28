from collections import deque

def solution(n, t, m, p):
    num = m*t+p # 필요한 숫자의 개수
    indices = [m*k+(p-1) for k in range(t)]
    tmp = ''
    i = 0
    while len(tmp) < num:
        tmp += converter(i,n)
        i += 1
    return ''.join(tmp[t] for t in indices)

def converter(i,x):
    dic = dict()
    for j in range(10,16):
        dic[j] = chr(ord('A')-10+j)
    
    tmp = deque([])
    while i >= x:
        tmp.appendleft(str(i%x) if i%x<10 else dic[i%x])
        i //= x
    tmp.appendleft(str(i%x) if i%x<10 else dic[i%x])
    return ''.join(tmp)
def solution(t, p):
    l = len(p)
    cnt = 0
    for i in range(len(t)-l+1):
        if int(t[i:i+l]) <= int(p):
            cnt += 1
    return cnt
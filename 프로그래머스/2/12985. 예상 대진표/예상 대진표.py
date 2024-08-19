def solution(n,a,b):
    big = max(a,b)
    small = min(a,b)
    cnt = 0
    while small != big:
        small = (small+1) >> 1
        big = (big+1) >> 1
        cnt += 1
    return cnt

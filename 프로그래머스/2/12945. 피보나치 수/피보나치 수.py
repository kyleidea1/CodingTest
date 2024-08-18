def solution(n):
    if n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        l = [0,1]
        for i in range(n-1):
            l.append(l[-1]+l[-2])
        ans = l[-1]
    return ans % 1234567
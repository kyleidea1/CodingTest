def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        cnt = 0
        l = 1
        r = 1
        summ = 0
        while l <= n//2 +1:
            if summ < n:
                summ += r
                r += 1
            elif summ > n:
                summ -= l
                l += 1
            else:
                cnt += 1
                summ -= l
                l += 1
        return cnt+1
            
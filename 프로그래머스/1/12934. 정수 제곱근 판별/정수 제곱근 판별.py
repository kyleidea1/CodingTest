def solution(n):
    i = 0
    while i**2 <= n:
        if n == i**2:
            return (i+1)**2
        i += 1
    return -1
def solution(n):
    f = [0] * 100001
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-2] + f[i-1]
    return f[n] % 1234567
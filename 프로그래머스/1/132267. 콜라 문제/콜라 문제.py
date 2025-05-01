def solution(a, b, n):
    ans = 0
    while n >= a:
        ans += b*(n//a)
        n = b*(n//a)+(n%a)
    return ans
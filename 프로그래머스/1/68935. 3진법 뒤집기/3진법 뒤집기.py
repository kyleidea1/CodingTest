def solution(n):
    s = ''
    while n >= 3:
        s += str(n%3)
        n //= 3
    s += str(n)
    s = s[::-1]
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])*(3**i)
        
    return sum
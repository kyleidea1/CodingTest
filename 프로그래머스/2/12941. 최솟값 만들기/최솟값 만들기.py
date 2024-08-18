def solution(A,B):
    ans = 0
    A.sort()
    B = sorted(B, reverse = True)
    while A:
        ans += A.pop() * B.pop()
    return ans
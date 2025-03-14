# def solution(n):
#     dp = [0] * (n+1)
#     dp[1] = 1
#     for i in range(2,n+1):
#         if i % 2 == 0:
#             dp[i] = min(dp[i//2],dp[i-1]+1)
#         else:
#             dp[i] = min(dp[i-1]+1,dp[i//2]+1)
#     return dp[n]

def solution(n):
    cnt = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            cnt += 1
    return cnt
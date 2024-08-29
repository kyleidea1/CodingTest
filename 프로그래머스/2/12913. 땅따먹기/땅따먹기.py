def solution(land):
    dp = [land[0]]
    for _ in range(len(land)-1):
        dp.append([0]*4)
    for i in range(1,len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][(j+1)%4], dp[i-1][(j+2)%4], dp[i-1][(j+3)%4]) + land[i][j]
    return max(dp[len(land)-1])
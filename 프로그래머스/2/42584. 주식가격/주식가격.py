def solution(prices):
    stack = []
    ans = [0]*len(prices)
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            p = stack.pop()
            ans[p] = i-p
        stack.append(i)
    while stack:
        p = stack.pop()
        ans[p] = len(prices)-p-1
    return ans
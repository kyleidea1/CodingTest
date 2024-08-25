def solution(a,b):
    ans = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            ans[i][j] = sum([a[i][k]*b[k][j] for k in range(len(a[0]))])
    return ans
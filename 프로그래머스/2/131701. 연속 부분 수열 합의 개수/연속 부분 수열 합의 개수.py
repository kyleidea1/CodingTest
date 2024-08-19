def solution(elements):
    sum = [[0]*len(elements) for _ in range(len(elements))]
    for i in range(len(elements)):
        sum[i][0] = elements[i]
        for j in range(1,len(elements)): # 1 2 3 4
            sum[i][j] = sum[i][j-1] + elements[(i+j)%len(elements)]
    return len(set([item for sublist in sum for item in sublist]))
def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        ans.append(tmp)
    return ans
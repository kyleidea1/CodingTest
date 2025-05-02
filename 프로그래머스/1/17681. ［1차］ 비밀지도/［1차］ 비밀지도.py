def trans(n,i):
    return '0'*(n-len(bin(i))+2) + bin(i)[2:]

def solution(n, arr1, arr2):
    matrix1 = [trans(n,i) for i in arr1]
    matrix2 = [trans(n,i) for i in arr2]
    result = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] == '1' or matrix2[i][j] == '1':
                result[i] += '#'
            else:
                result[i] += ' '
    return result
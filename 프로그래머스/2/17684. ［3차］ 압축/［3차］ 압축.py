def solution(msg):
    dic = dict()
    for i in range(1,27):
        dic[chr(ord('A')+i-1)] = i
    ans = []
    i = 0
    tmp = ''
    while i < len(msg):
        tmp += msg[i]
        if tmp in dic.keys():
            i += 1
            if i == len(msg):
                ans.append(dic[tmp])
        else:
            dic[tmp] = len(dic) + 1
            ans.append(dic[tmp[:-1]])
            tmp = ''

    return ans
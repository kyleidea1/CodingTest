def solution(s):
    dic = dict()
    l = [-1]*len(s)
    for i in range(len(s)):
        if s[i] in dic.keys():
            l[i] = i - dic[s[i]]
        dic[s[i]] = i
    return l
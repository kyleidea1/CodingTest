def solution(s):
    ss = s[2:-2].split('},{')
    sss = [list(s.split(',')) for s in ss]
    ssss = sorted(sss, key = lambda x:len(x))
    l = []
    for i in ssss:
        for j in i:
            if int(j) not in l:
                l.append(int(j))
    return l
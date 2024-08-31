def solution(skill, skill_trees):
    dic = dict(zip(skill,range(1,len(skill)+1)))
    cnt = 0
    for st in skill_trees:
        if is_valid([dic[i] for i in st if i in dic.keys()]):
            cnt += 1
    return cnt

def is_valid(l):
    if not l:
        return True
    else:
        return l[0] == 1 and all(l[i+1] == l[i]+1 for i in range(len(l)-1))
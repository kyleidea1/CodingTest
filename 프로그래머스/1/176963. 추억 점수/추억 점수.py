def solution(name, yearning, photo):
    dic = dict(zip(name,yearning))
    return [sum([dic[x] for x in l if x in dic]) for l in photo]
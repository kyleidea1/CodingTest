def solution(n, words):
    dic = dict()
    dic[words[0]] = True
    for i in range(1,len(words)):
        if words[i] in dic or words[i][0] != words[i-1][-1]:
            loser = n if (i+1)%n == 0 else (i+1)%n
            turn = i//n + 1
            return [loser, turn]
        else:
            dic[words[i]] = True
    return [0,0]
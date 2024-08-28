def solution(word):
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    weight = {'0':781, '1':156, '2':31, '3':6, '4':1}
    ans = len(word)
    delta = 0
    for i in range(len(word)):
        delta += dic[word[i]] * weight[str(i)]
    return ans + delta


    
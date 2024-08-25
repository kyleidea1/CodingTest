from collections import Counter

def solution(want, number, discount):
    target_dic = dict(zip(want,number))
    cnt = 0
    for i in range(len(discount)-sum(number)+1):
        cnt_window = Counter(discount[i:sum(number)+i])
        if target_dic == cnt_window:
            cnt += 1
    return cnt
        
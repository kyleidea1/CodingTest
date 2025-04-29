def change(w):
    s = ''
    for i in range(len(w)):
        s += (w[i].upper() if i%2 == 0 else w[i].lower())
    return s

def solution(s):
    w_list = list(s.split(' '))
    ans = ''
    for w in w_list:
        ans += change(w)
        ans += ' '
    return ans[:-1]
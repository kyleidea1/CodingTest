from collections import Counter

def solution(str1, str2):
    s1 = Counter(make_pairs(str1))
    s2 = Counter(make_pairs(str2))
    uni_len = sum(list((s1|s2).values()))
    inter_len = sum(list((s1&s2).values()))
    ans = int((inter_len / uni_len) * 65536) if uni_len != 0 else 65536
    return ans

def make_pairs(s):
    pairs = [s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()]
    return pairs
    
        
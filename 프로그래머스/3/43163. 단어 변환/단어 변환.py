from collections import deque

def solution(begin, target, words):
    q = deque([(begin,0)])
    dic = dict()
    for w in words:
        dic[w] = True
        
    while q:
        cur, cnt = q.popleft()
        cnt += 1
        for w in dic.keys():
            if dic[w] and compare(cur,w):
                if w == target:
                    return cnt
                q.append((w,cnt))
                dic[w] = False
    return 0

def compare(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return True if cnt == 1 else False
    
    
    
    
    
    
    
    
# def solution(begin, target, words):
#     q = deque()
#     visited = []
#     cnt = 0
#     q.append((begin,cnt))
    
#     while q:
#         cur,cnt = q.popleft()
#         cnt += 1
#         for w in words:
#             if w not in visited:
#                 if check(cur,w):
#                     if w == target:
#                         return cnt
#                     else:
#                         q.append((w,cnt))
#                         visited.append(w)
#     return 0

# def check(word1,word2):
#     cnt = 0
#     for i in range(len(word1)):
#         cnt += (0 if word1[i] == word2[i] else 1)
#     return cnt == 1
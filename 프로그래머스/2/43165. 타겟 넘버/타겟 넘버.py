from collections import deque
def solution(nums, target):
    level = [0]
    
    for i in range(len(nums)):
        tmp = []
        for j in range(len(level)):
            tmp.append(level[j] + nums[i])
            tmp.append(level[j] - nums[i])
        level = tmp
        
    return level.count(target)
    
    
    
    
    
    
    
    
    
    
    
    
#     leaves = [0]
#     ans = 0
    
#     for n in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + n)
#             tmp.append(parent - n)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             ans += 1
#     return ans
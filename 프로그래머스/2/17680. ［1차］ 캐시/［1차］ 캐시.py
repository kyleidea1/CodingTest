from collections import deque

def solution(cacheSize, cities):
    cache = deque([cities[i].lower() for i in range(cacheSize)])
    cost = 5 * cacheSize
    
    for i in range(cacheSize,len(cities)):
        if cities[i].lower() in cache:
            del(cache(cache.index(cities[i])))
            cost += 1
        else:
            cost += 5
            cache.popleft()
        cache.append(cities[i].lower())
        
    return cost
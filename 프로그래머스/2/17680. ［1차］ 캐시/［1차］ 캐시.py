from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    cost = 0
    
    for i in range(len(cities)):
        if cities[i].lower() not in cache:
            cache.append(cities[i].lower())
            if len(cache) > cacheSize:
                cache.popleft()
            cost += 5
        else:
            cache.remove(cities[i].lower())
            cache.append(cities[i].lower())
            cost += 1
    return cost

def solution(sizes):
    for s in sizes:
        s.sort()
    return max([sizes[i][0] for i in range(len(sizes))]) * max([sizes[i][1] for i in range(len(sizes))])
def solution(n):
    num_of_one = bin(n)[2:].count('1')
    while True:
        n += 1
        new = bin(n)[2:].count('1')
        if new == num_of_one:
            break
    return n
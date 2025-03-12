def solution(n):
    num_of_one = str(bin(n)[2:]).count('1')
    while True:
        n += 1
        if bin(n).count('1') == num_of_one:
            break
    return n
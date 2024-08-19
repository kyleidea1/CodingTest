def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow%i == 0:
            if brown + yellow == (i+2) * ((yellow//i)+2):
                break         
    return [i+2,((yellow//i)+2)] if i+2 > ((yellow//i)+2) else [((yellow//i)+2), i+2]
            
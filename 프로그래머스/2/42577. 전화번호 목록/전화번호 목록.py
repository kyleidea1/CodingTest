def solution(phone_book):
    phone_book.sort()
    dic = dict()
    for num in phone_book:
        temp = ""
        for n in num:
            temp += n
            if temp in dic.keys():
                return False
        dic[num] = True
    return True
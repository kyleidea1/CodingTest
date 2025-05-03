def solution(a, b):
    month_list = list(range(12))
    days_of_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    dic1 = dict(zip(month_list, days_of_month))
    
    day_list = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    dic2 = dict(zip(list(range(7)), day_list))
    
    days = 0
    for i in range(a-1):
        days += dic1[i]
    days += (b-1)
    day = days % 7
    return dic2[day]
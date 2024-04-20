def solution(a, b):
    
    week = {0: "THU", 1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED"}
    months = {}
    k = 0
    
    for i in range(1, 13):
        if i <= 7:
            if i == 2: #2월일 경우
                months[i] = 29
            elif i % 2 == 1: #1,3,5,7월
                months[i] = 31
            else: #2,4,6월
                months[i] = 30
        else:
            if i % 2 == 1: #9,11월
                months[i] = 30
            else: #8,10,12월
                months[i] = 31
    
    for i in range(1, a):
        k = k + months[i]
    
    k = k + b
        
    k = k % 7
    
    answer = week[k]
    return answer
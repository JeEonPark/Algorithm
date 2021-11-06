def solution(n, lost, reserve):
    answer = 0
    
    for i in range(1,n+1): 
        if i not in lost: #안잃어버린 애들
            answer += 1
        else:
            if i in reserve: #잃어버렸는데 리저브있는 애들
                reserve.remove(i)
                lost.remove(i)
                answer += 1

    for i in lost: #잃어버린놈
        if i-1 in reserve:  #잃어버린놈한테 주는 애
            answer += 1
            reserve.remove(i-1)
            
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
        
        print(lost)

    return answer #답

print("Solution : " + str(solution(5, [3,1], [2,4,5])))
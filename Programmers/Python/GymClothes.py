def solution(n, lost, reserve):
    
    can_play=n-len(lost)
    
    index=[]
    
    #자기자신이 가지고 있는 경우
    for i in range(0, len(lost)):
        print(lost[i])
        if lost[i] in reserve:
            can_play=can_play + 1
            index.append(lost[i])
            reserve.remove(lost[i])
            
    for i in index:
        lost.remove(i)
    
    #한쪽에서만 받을 수 있는 경우
    for i in lost:
        #n일경우
        if i==n:
            if n-1 in reserve:
                can_play=can_play + 1
                lost.remove(n)
                reserve.remove(n-1)
        else:
            if i-1 in reserve and not i+1 in reserve:
                can_play=can_play + 1
                lost.remove(i)
                reserve.remove(i-1)
            elif i+1 in reserve and not i-1 in reserve:
                can_play=can_play + 1
                lost.remove(i)
                reserve.remove(i+1)
                
    #나머지
    for i in lost:
        if i-1 in reserve:
            can_play=can_play + 1
        elif i+1 in reserve:
            can_play=can_play + 1
        
    
    answer = can_play
    return answer
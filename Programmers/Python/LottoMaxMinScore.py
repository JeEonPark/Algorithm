def solution(lottos, win_nums):
    
    #지워진 숫자들의 갯수 파악
    zero_count = 0
    for i in lottos:
        if i == 0:
            zero_count = zero_count + 1
    print(zero_count)
    
    #보이는 것 중 맞춘 갯수 파악
    correct = 0
    for i in lottos:
        for j in win_nums:
            if i == j: 
                correct = correct + 1
    print(correct)
    
    #0을 생각 안했을 때 (최저 순위)
    low = correct
    
    #0이 다 맞았을 경우 (최고 순위)
    high = correct + zero_count
    
    #맞은 갯수를 순위로 변환
    low = 7 - low
    high = 7 - low
    
    answer = [low, high]
    return answer
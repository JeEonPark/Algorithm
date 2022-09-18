def solution(answers):
    
    answer = []
    
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    supo1_count = 0
    supo2_count = 0
    supo3_count = 0
    
    for i in range(0, len(answers)):
        if answers[i] == supo1[i%5]:
            supo1_count += 1
        if answers[i] == supo2[i%8]:
            supo2_count += 1
        if answers[i] == supo3[i%10]:
            supo3_count += 1
    
    if(supo1_count >= supo2_count):
        if(supo1_count >= supo3_count):
            answer.append(1)
    if(supo2_count >= supo1_count):
        if(supo2_count >= supo3_count):
            answer.append(2)
    if(supo3_count >= supo2_count):
        if(supo3_count >= supo1_count):
            answer.append(3)
    
    
    
    return answer
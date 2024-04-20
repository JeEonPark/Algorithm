def solution(periods, payments, estimates):
    answer = [0 for i in range(0, 2)]

    for i in range(0, len(periods)):
        peri = periods[i]
        now_vip = False;
        next_vip = False;

        # 이번 달 vip 인지 판단
        now_all_pay = sum(payments[i])
        if peri < 24:
            now_vip = False
        elif peri < 60 and now_all_pay >= 900000:
            now_vip = True
        elif peri >= 60 and now_all_pay >= 600000:
            now_vip = True
        else:
            now_vip = False

        # 다음 달 vip 인지 판단
        next_all_pay = sum(payments[i]) - payments[0] + estimates[i]
        if peri + 1 < 24:
            next_vip = False
        elif peri + 1 < 60 and next_all_pay >= 900000:
            next_vip = True
        elif peri + 1 >= 60 and next_all_pay >= 600000:
            next_vip = True
        else:
            next_vip = False

        # 최종 판단
        if not now_vip and next_vip:
            answer[0] = answer[0] + 1
        elif now_vip and not next_vip:
            answer[1] = answer[1] + 1
    
    return answer

    
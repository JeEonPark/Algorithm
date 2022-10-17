from collections import Counter

def solution(array):
    cnt = Counter(array)
    cnt.most_common()
    mode = cnt.most_common(2)
    if len(mode) > 1:
        if mode[0][1] == mode[1][1]:
            return -1

    return mode[0][0]
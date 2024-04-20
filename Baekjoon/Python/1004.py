import math


def dot_to_dot(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2) + (y2 - y1)**2)


def if_dot_in_circle(x, y, a, b, r):
    if(dot_to_dot(x, y, a, b) > r):
        return False
    elif(dot_to_dot(x, y, a, b) < r):
        return True


t_case = int(input())
result = []

for i in range(0, t_case):
    from_to_dot = list(map(int, input().split()))  # 출발지와 목적지의 좌표
    circles_loop = int(input())  # 원의 갯수
    count = 0
    for j in range(0, circles_loop):
        circle = list(map(int, input().split()))
        start_dot_in_circle = if_dot_in_circle(from_to_dot[0], from_to_dot[1], circle[0], circle[1], circle[2])
        end_dot_in_circle = if_dot_in_circle(from_to_dot[2], from_to_dot[3], circle[0], circle[1], circle[2])

        if(start_dot_in_circle and not end_dot_in_circle):
            count += 1
        elif(not start_dot_in_circle and end_dot_in_circle):
            count += 1
    result.append(count)

for i in list(result):
    print(i)
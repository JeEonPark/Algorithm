t_case = int(input())
result = []

for i in range(0, t_case):
    buildings_and_rules_times = list(map(int, input().split())) #빌딩 갯수, 규칙 갯수
    build_time = list(map(int, input().split())) #각 빌딩 별 건설 시간
    rules = []
    for j in range(0, buildings_and_rules_times[1]):
        temp = list(map(int, input().split()))
        rules[j] = {}

    is_building_done = [False for i in range(buildings_and_rules_times[0])]

    second = 0
    
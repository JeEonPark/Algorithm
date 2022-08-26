factScore = [
    21658,
    19532,
    19485,
    17879,
    15330,
    14798,
    13790,
    11709,
    11325,
    11809,
    10275,
    9943,
    9620,
    8761,
    8951,
    8848,
    7685,
    6318,
    6879,
    6117,
    5480,
    4664,
    5633,
    4290,
    3517,
    4150,
    2361,
    2295,
    1827
]

cuda = [
    8064,
    7680,
    7872,
    6528,
    4352,
    4608,
    4416,
    3072,
    2944,
    3648,
    2560,
    2304,
    2635,
    1882,
    2176,
    2688,
    1920,
    1129,
    1788,
    1035,
    1035,
    941,
    2070,
    941,
    658,
    1506,
    565,
    752,
    565
]

sumAbsMinus = []
averageDXDY = 12332/28
rank = range(28, -1, -1)
pValue = []
for index in range(0, 29):
    pValue.append((factScore[index]-cuda[index])-averageDXDY*rank[index])

for p in pValue:
    # Y 값 구해주기
    y = []
    for index1 in range(0,29):
        y.append(averageDXDY*rank[index1]+p)
    # 예측 3DMARK 값
    predictScore = []
    for index2 in range(0,29):
        predictScore.append(y[index2]+cuda[index2])
    # adb(예측-실제) 구해서 배열
    absMinus = []
    for index3 in range(0,29):
        absMinus.append(abs(predictScore[index3]-factScore[index3]))
    sumAbsMinus.append(sum(absMinus))

print(min(sumAbsMinus))
print(sumAbsMinus.index(min(sumAbsMinus)))
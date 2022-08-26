factScore = [
    21658,
    19485,
    19532,
    17879,
    14798,
    13790,
    15330,
    11809,
    9620,
    11709,
    11325,
    5633,
    8848,
    10275,
    8761,
    6879,
    9943,
    8951,
    4150,
    7685,
    6318,
    6117,
    5480,
    4664,
    4290,
    2295,
    3517,
    2361,
    1827
]

cuda = [
    8064,
    7872,
    7680,
    6528,
    4608,
    4416,
    4352,
    3648,
    3584,
    3072,
    2944,
    2816,
    2688,
    2560,
    2560,
    2432,
    2304,
    2176,
    2048,
    1920,
    1536,
    1408,
    1408,
    1280,
    1280,
    1024,
    896,
    768,
    768
]

sumAbsMinus = []
averageDXDY = 12535/28
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
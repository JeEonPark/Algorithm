import random
from subprocess import list2cmdline

list = []
list.append("김형진")
list.append("정한나")
list.append("이소윤")
list.append("김정혁")
list.append("이윤지")
list.append("옥채현")
list.append("배현아")
list.append("김홍진")

num = []
for value in list:
    tempNum = random.randrange(1, len(list)+1)
    while tempNum in num:
        tempNum = random.randrange(1, len(list)+1)
    num.append(tempNum)

for value in range(len(list)):
    print(str(list[value]) + " : " + str(num[value]))
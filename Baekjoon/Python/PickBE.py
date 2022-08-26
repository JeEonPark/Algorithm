import random
from subprocess import list2cmdline

list = []
list.append("박용호")
list.append("손병욱")
list.append("장찬희")
list.append("최유진")

num = []
for value in list:
    tempNum = random.randrange(1, len(list)+1)
    while tempNum in num:
        tempNum = random.randrange(1, len(list)+1)
    num.append(tempNum)

for value in range(len(list)):
    print(str(list[value]) + " : " + str(num[value]))
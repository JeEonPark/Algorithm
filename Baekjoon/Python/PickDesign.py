import random
from subprocess import list2cmdline

list = []
list.append("이정향")
list.append("한수현")

num = []
for value in list:
    tempNum = random.randrange(1, len(list)+1)
    while tempNum in num:
        tempNum = random.randrange(1, len(list)+1)
    num.append(tempNum)

for value in range(len(list)):
    print(str(list[value]) + " : " + str(num[value]))
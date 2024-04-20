test_count = int(input())

def factorial(p):
    if(p > 1):
        return p * factorial(p - 1)
    else:
        return 1

n, m = [], []
for i in range(0, test_count):
    tmp_n, tmp_m = map(int, input().split())
    n.append(tmp_n)
    m.append(tmp_m)

for i in range(0, test_count):
    print(int(factorial(m[i])/(factorial(n[i])*(factorial(m[i]-n[i])))))

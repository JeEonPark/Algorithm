dp = [0 for i in range(41)]

def fibonacci(n):
    if n == 0:
        dp[0] = 0;
        return 0
    elif n == 1:
        dp[1] = 1;
        return 1;
    if dp[n] != 0:
        return dp[n];
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]

res = int(input())
arr = []

for i in range(0, res):
    arr.append(int(input()))

for i in range(0, res):
    fibonacci(arr[i])
    if arr[i] == 0:
        print("1 0")
    elif arr[i] == 1:
        print("0 1")
    else:
        fibonacci(arr[i])
        print(str(dp[arr[i]-1]) + " " + str(dp[arr[i]]))
        

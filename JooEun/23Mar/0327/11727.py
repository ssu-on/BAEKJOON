n = int(input())

dp = [0, 1, 3] + [0]*(n)
if n >=3:
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2])%10007

print(dp[n])
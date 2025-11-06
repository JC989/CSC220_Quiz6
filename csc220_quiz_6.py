#322. Coin Change
#You are given an integer array coins representing coins of 
# different denominations and an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount. If that 
# amount of money cannot be made up by any combination of the coins, return -1.
#You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] 
        for j in range(1, amount + 1):
           dp.append(float('inf'))
           for coin in coins:
               dp[j] = min(dp[j],dp[j-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
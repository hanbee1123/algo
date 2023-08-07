"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

#Using BFS

from collections import deque
class Solution:
    def coinChange(self, coins, amount):
        if amount ==0:
            return 0

        depth = 0
        q = deque([(amount,depth)])
        seen = set()
        while q:
            val,depth = q.popleft()
            for c in coins:
                new_val = val-c
                if new_val == 0:
                    return depth+1
                
                if new_val not in seen and new_val > 0:
                    seen.add(new_val)
                    q.append((new_val,depth+1))
        return -1


# Using DP bottomup
class Solution:
    def coinChange(self, coins, amount):
        dp= [amount+1] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==amount+1 else dp[-1]
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i + len(w)] == w:#check if we have enough characters left to compare
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]
if __name__ == "__main__":
    s = "cars"
    wordDict = ["car","ca","rs"]
    sa = Solution()
    print(sa.wordBreak(s,wordDict))
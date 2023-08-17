class Solution:
    def wordBreak(self, s, wordDict):
        self.length = len(s)

        memo = {}
        def dfs(s,worddict,idx):
            if idx in memo:
                return memo[idx]


            if idx == self.length:
                memo[idx] = True
                return True
            
            for w in worddict:
                if s[:len(w)] == w:
                    if dfs(s[len(w):], worddict, idx+len(w)) == True:
                        return True
            memo[idx] = False
            
        return dfs(s, wordDict,0)
if __name__ == "__main__":
    s = "cars"
    wordDict = ["car","ca","rs"]
    sa = Solution()
    print(sa.wordBreak(s,wordDict))
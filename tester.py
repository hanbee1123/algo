class Solution:
    def longestPalindrome(self, s):
        self.s = s
        self.final_result = ''

        def check_ss(s):
            return s == s[::-1]


        def dfs(idx, substring):
            if check_ss(substring) == True:
                self.final_result = max(self.final_result, substring, key=len)

            if idx <= len(self.s)-1:
                dfs(idx+1, substring+self.s[idx])
            return
        for i in range(len(s)):
            dfs(i,'')
        print(self.final_result)
if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome("babad")

class Solution:
    def letterCombinations(self, digits):
        self.letters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }   
        self.return_val = []
        if len(digits)==0:
            return self.return_val
        def dfs(output,digits):
            if len(digits)==0:
                self.return_val.append(output)
                return
            
            if digits[0] in self.letters:
                for i in self.letters[digits[0]]:
                    dfs(output+i, digits[1:])
            else:
                dfs(output, digits[1:])
                    
        dfs('',digits)
        return self.return_val
            


            
            


if __name__ == "__main__":
    s = Solution()

    print(s.letterCombinations("23"))
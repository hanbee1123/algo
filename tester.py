class Solution:
    def combinationSum(self, candidates,target):
        #dfs(depth first search (깊이 우선 탐색))
        self.return_val = []
        self.candidates = candidates
        lister = []
        def dfs(target,lister):
            if target == 0:
                self.return_val.append(lister.copy())

            elif target < 0:
                return
            else:
                for c in self.candidates:
                    lister.append(c)
                    if sorted(lister) not in self.return_val:
                        dfs(target-c, sorted(lister))
                    lister.pop()
            return


        dfs(target,lister)
        return self.return_val

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    a = Solution()
    print(a.combinationSum(candidates,target))

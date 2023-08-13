# 46. Permutations
# Medium
# 17.5K
# 279
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


class Solution:
    def permute(self, nums):
        """
        answer using DFS
        
        general idea:
        - perform a loop through num in nums.
        - Then while looping through each of them perform a DFS. 
        - For base case, append permutation into return value.
        """

        return_val=[]

        def dfs(nums, var):
            # if length of variable == nums
            if len(var) == len(nums):
                return_val.append(var.copy())
            # else: perform loop
            else:
                for n in nums:
                # make sure we don't perform a loop with numbers already added in var.
                    if n not in var:
                        new_var = var.copy()
                        new_var.append(n)
                        dfs(nums,new_var)

        for num in nums:
            var = [num]
            dfs(nums, var)
        
        return return_val

#O(n!)
#how can we optimize this?
# how can we use less memory?
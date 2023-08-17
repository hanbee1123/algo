"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

"""
class Solution:
    def canPartition(self, nums):
        """
        Calculate the sum of every subset and check if it meets our target (sum(nums)//2)
        """
        target = sum(nums)//2

        if sum(nums)%2 != 0:
            return False

        memo = set()
        memo.add(0)

        for num in nums:
            new_memo = memo.copy()
            for m in new_memo:
                if m+num not in memo:
                    memo.add(m+num)
                if m+num == target:
                    return True
        return False

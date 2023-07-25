def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    even_sum = 0
    odd_sum = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            even_sum = max(odd_sum, even_sum + nums[i])
        else:
            odd_sum = max(even_sum, odd_sum + nums[i])
    
    return max(even_sum, odd_sum)

if __name__ == "__main__":
    print(rob([100,1,1,1,2,100]))


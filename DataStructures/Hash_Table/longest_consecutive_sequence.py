"""
문제:
정렬되어 있지 않은 정수현 배열 nums가 주어졌다. nums원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환하시오

input: nums =[100,4,200,1,3,2]
output: 4 (가장 긴 연속된 수 1,2,3,4)

문제 해결:
O(nlogn) method:
#1. sort the nums
#2. then from beginning consecutive sequence. 


O(n) method using hash table:
#1. 100,4,200,1,3,2

[101:T, 5:T, 201:T, 2:T, 4:T, 3:T]
# While True, check if element in array has +1 value in dictionary.

Dummy code:

memo = {}
for i in input:
    memo[i] = 'dummy'

counter += 1
max_counter = 0

for i in input:
    while i+counter in memo:
        i += 1
        max_counter = max(counter, max_counter)

return max_counter


edge cases:
- what if no input?
    - 0 will be retuned 
- what if 1 input?
    - max_counter will be returned = 1
- what is no consecutive?
    - max_counter will be returned = 1
"""

def lcs(nums):
    memo = {}
    # put values in nums as keys in hash table
    for i in nums:
        memo[i] = True
    
    max_counter = 0
    for i in nums:
        if i-1 not in memo:
            counter = 1
            while i + counter in memo:
                counter += 1
            max_counter = max(counter, max_counter)
    return max_counter

if __name__ == "__main__":
    print(lcs([-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]))

    

#correct answer:
# longest = 0
# num_dict = {}

# for num in nums:
#     num_dict[num] = True

# for num in num_dict:
#     if num-1 not in num_dict:
#         cnt = 1
#         target = num+1
#         while target in num_dict:
#             target += 1
#             cnt += 1
#         longest = max(longest,cnt)
#     return longest
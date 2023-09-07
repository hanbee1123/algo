
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution:
#     def findAnagrams(self, s: str, p: str):
#         result = []
#         for i in range(len(s)-len(p)+1):
#             if self.checkAnagram(s[i:i+len(p)],p):
#                 result.append(i)
#         return result

#     def checkAnagram(self, s, p):
#         counts = {}
#         for c1, c2 in zip(s,p):
#             if c1 in counts.keys():
#                 counts[c1] += 1
#             else:
#                 counts[c1]=1
#             if c2 in counts.keys():
#                 counts[c2]-=1
#             else:
#                 counts[c2]=-1

#         for count in counts.values():
#             if count!=0:
#                 return False
#         return True
        



#     def findAnagrams(self, string: str, anagram: str):
        
#         # sort the anagram and store it back to itself
#         anagram = ''.join(sorted(anagram))
        
#         # this will represent the current "window"
#         window_string = ''
        
#         # create a list variable to store the start indices, this is what we will return
#         start_indices = []
        
#         # initialize the start of the window at index 0
#         window_start = 0
        
#         # iterate through the entire string
#         for char in string:

#             # slide the right side of the window (equivalent to adding the next character to current string)
#             window_string += char
        
#             # start checking the window once the window size is size of anagram
#             if len(window_string) == len(anagram):

#                 # sort the current string in the window and check if it equals the anagram
#                 if ''.join(sorted(window_string)) == anagram:
                    
#                     # FOUND AN ANAGRAM! 
#                     # append the window start index to start_indices
#                     start_indices.append(window_start)

#                 # remove the leftmost character of the window and slide the left side of the window
#                 window_string = window_string[1:]
#                 window_start += 1

#         return start_indices

# """
# First, we have to create a hash map with letters from p as keys and its frequencies as values. 
# Then, we start sliding the window [0..len(s)] over the s. 
# Every time a letter gets out of the window, we increase the corresponding counter in the hashmap, 
# and when a letter gets in the window - we decrease.
# As soon as all counters in the hashmap become zeros we encountered an anagram.

# Time: O(n) - one pass over the p, on pass for s, and for every letter in s we iterate over values in hashmap (maximum 26)
# Space: O(1) - hashmap with max 26 keys
# """

    def findAnagramss(self, s: str, p: str):
        result = []
        hm = {}
        for ch in p:
            if ch in hm:
                hm[ch] -= 1
            else:
                hm[ch] = -1
        window = ''
        for i in range(0,len(s)):
            window += s[i]
            if s[i] in hm:
                hm[s[i]] += 1

            
            if len(window) == len(p):
                #check for anagram
                if all(v ==0  for v in hm.values()):
                    result.append(i-len(p)+1)
                
                if window[0] in hm:
                    hm[window[0]] -= 1

                window = window[1:]

        return result

        

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagramss("cbaebabacd","abc"))
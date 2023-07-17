'''
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

TIP: USE THE SLIDING WINDOW TECHNIQUE!
'''

def substring_length(s):
    # For this function to work, you need to use the sliding window method
    str_list = []
    max_val = 0
    for i in s:
        if i in str_list:
            str_list = str_list[str_list.index(i)+1:]
        else:
            str_list.append(i)
            max_val = max(max_val, len(str_list))
    return max_val
        

def test_substring_length():
    try:
        assert substring_length('abcabcbb') == 3
    except: 
        raise AssertionError("Assertion not working bro")
    else:
        return True

if __name__ == "__main__":
    print(test_substring_length())
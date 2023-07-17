"""
문제:
'(){}[]' 를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.

input: s = ")(" 
output: false

input: s = '([]}'
output: false


코드 설계:
# create a hashmap for each closing parentheses.


#if length is an odd number return false

# create a stack.
# whenever a closing parentheses is met, check whether the top of the stack is an opening parentheses that is same as the closing one.
if yes:
pop the stack.
else:
error

#after all loop: if length of stack > 0, return false.

"""

def isValid(s: str) -> bool:
# create a hashmap for each closing parentheses.
    hashmap = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

#if length is an odd number return false
    if len(s) % 2 == 1:
        return False

    else:
# whenever a closing parentheses is met, check whether the top of the stack is an opening parentheses matches closing one.    
        stack = []
        for i in s:
            if i in hashmap.keys():
                if not stack or stack.pop() != hashmap[i]:
                    return False
            else:
                stack.append(i)

        if len(stack) != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    print(isValid("()"))



""""
2nd method
"""
def isValid(s:str):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop()!=i:
            return False
    # basically means if stack != None, return True else False.
    return not stack

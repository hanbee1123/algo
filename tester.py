def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i=="[" or i== "{":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return stack is None

if __name__=="__main__":
    print(isValid("]"))
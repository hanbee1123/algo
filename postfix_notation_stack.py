# infix notation is the normal notation we see
# (A+B) * (B+C)
# postfix notation is where the notations have specific orders
# AB + BC + *
# In this algorithm, we will learn how to change infix notation to postfix notation using STACK
# eg. A*B+C = AB*C+

# The algorithm will work as follows:
# 1. Will loop through string
# 2. If character is NOT an operator, Leave it as it is
# 3. Else, if character IS operator, Push it to stack
# 4. If character is '(' operator, push it to the stack and pop everything once it meets ')' operator

class ArrayStack:
    def __init__(self):
        self.data = []
    def push(self,data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size() == 0
    
def change_to_postfix(expression):
    '''This function changes an infix notation to a postfix notation
    
    param expression: A infix notation which will be transformed to a postfix notation
    return: A postfix notation of the expression

    >>> change_to_postfix('(A+B)*(B+C)') 
    'AB+ BC+ *'
    '''
    postfix = ArrayStack()
    answer = ""
    # First set the priority of operators 
    operator = {
        '*':3
        ,'/':3
        ,'+':2
        ,'-':2
        ,'(':1
    }

    # Loop through the infix notation expression
    for char in expression:
        # If the character is an alphabet append it to the answer
        if char.isalpha():
            answer += char
        # If the character is an opening bracket, push it to stack
        elif char == '(':
            postfix.push(char)
        # If the character is a closing bracket, pop everthing until '(' and append it to the answer
        elif char == ')':
            while postfix.peek() != '(':
                answer += postfix.peek()
                postfix.pop()
            if postfix.peek() == '(':
                postfix.pop()
        # If the character is an operator, 
        elif char in operator:
            # If the postfix is not empty compare the value of the operators
            if not postfix.is_empty():
                # if the character has a higher value than the peek of stack OR is '(', push it to the peek of stack
                if operator[char] > operator[postfix.peek()] or char == '(':
                    postfix.push(char)
                # if the character has a lower value thann the peek of stack and is NOT '(' keep appending the peek
                elif operator[char]<=operator[postfix.peek()] and char != '(':
                    while operator[char]<= operator[postfix.peek()]:
                        answer += postfix.peek()
                        postfix.pop()
                        if postfix.is_empty():
                            postfix.push(char)
                            break
                # if the stack is empty, push the operator to the stack.
            else:
                postfix.push(char)
        # If the character is NOT an operator and NOT an alphabet, raise value error
        else: 
            raise ValueError('There is an inappropriate character in the expression')
    # When the loop is over but the stack is not empty, push every value in the stack to the answer
    while not postfix.is_empty() and postfix.peek() != '(':
        answer += postfix.peek()
        postfix.pop()
    return answer

if __name__ == "__main__":
    expression = 'A+B*C-D'
    print(change_to_postfix(expression))
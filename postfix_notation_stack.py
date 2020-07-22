# infix notation is the normal notation we see
# (A+B) * (B+C)
# postfix notation is where the notations have specific orders
# AB + BC + *
# In this algorithm, we will learn how to change infix notation to postfix notation using STACK
# eg. A*B+C = AB*C+

# The algorithm will work as follows:
# 1. Will loop through string
# 2. If character is NOT an self.operator, Leave it as it is
# 3. Else, if character IS self.operator, Push it to stack
# 4. If character is '(' self.operator, push it to the stack and pop everything once it meets ')' self.operator

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

class PostFix:
    operator = {
            '*':3
            ,'/':3
            ,'+':2
            ,'-':2
            ,'(':1
        }

    def split_tokens(self, expression):
        '''This function splits string values into list of tokens
            
        param expression: expression in string
        return: expression in list

        >>> split_tokens('12+13*153')
        [12, '+', 13, '*', 153]
        '''
        tokens = []
        val = 0
        val_processing = False
        # loop through string
        for c in expression:
            if c == ' ':
                pass
            # if character is an integer
            if c in '0123456789':
                # make the string integer value to a whole number
                val = val * 10 + int(c)
                val_processing = True
            # If the character is an operator, just append it to the list
            else:
                if val_processing:
                    tokens.append(val)
                    val = 0
                val_processing = False
                tokens.append(c)
        if val_processing:
            tokens.append(val)
        
        return tokens

    def change_to_postfix(self, expression):
        '''This function changes an infix notation to a postfix notation
        
        param expression: A infix notation which will be transformed to a postfix notation
        return: A postfix notation of the expression

        >>> change_to_postfix('(A+B)*(B+C)') 
        'AB+ BC+ *'
        '''
        expression = self.split_tokens(expression)
        postfix = ArrayStack()
        answer = []
        # Loop through the infix notation expression
        for char in expression:
            # If the character is an alphabet append it to the answer
            if type(char) is int:
                answer.append(char)
            # If the character is an opening bracket, push it to stack
            elif char == '(':
                postfix.push(char)
            # If the character is a closing bracket, pop everthing until '(' and append it to the answer
            elif char == ')':
                while postfix.peek() != '(':
                    answer.append(postfix.peek())
                    postfix.pop()
                if postfix.peek() == '(':
                    postfix.pop()
            # If the character is an self.operator, 
            elif char in self.operator:
                # If the postfix is not empty compare the value of the self.operators
                while not postfix.is_empty() and self.operator[char]<=self.operator[postfix.peek()]:
                    answer.append(postfix.peek())
                    postfix.pop()
                postfix.push(char)
            else: 
                raise ValueError('There is an inappropriate character in the expression')
        # When the loop is over but the stack is not empty, push every value in the stack to the answer
        while not postfix.is_empty() and postfix.peek() != '(':
            answer.append(postfix.peek())
            postfix.pop()
        return answer


    def calculate_postfix(self, expression):
        '''This function calculates the value of the postfix notation
        
        param expression: An infix notation formed with real numbers
        return: a number value

        >>> calculate_postfix(12+2*3-4)
        '3'
        '''
        postfix_notation = self.change_to_postfix(expression)
        stack = ArrayStack()
        for char in postfix_notation:
            if type(char) is int:
                stack.push(char)
            elif char in self.operator:
                first_num = stack.peek()
                stack.pop()
                second_num = stack.peek()
                stack.pop()
                value = eval(str(second_num)+ char + str(first_num))
                stack.push(value)
            else:
                raise ValueError('Your expression consists of a value that is not an operator or a number')
        return stack.peek()
    

if __name__ == "__main__":
    expression = '12+2*3-4'
    postfix = PostFix()
    print(postfix.split_tokens(expression))
    print(postfix.change_to_postfix(expression))
    print(postfix.calculate_postfix(expression))



class ArrayStack:

    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        return self.data.pop()

    def push(self, item):
        return self.data.append(item)
    
    def peek(self):
        return self.data[-1]

def solution(expressions):
    match = {
        ')':'('
        , ']':'['
        , '}':'{'
    }
    S = ArrayStack()
    for c in expressions:
        if c in '([{':
            S.push(c)
        elif c in ')]}':
            if S.is_empty():
                return False
            else:
                t = match[c]
                if t!=S.pop():
                    return False
    return True

if __name__ == "__main__":
    print(solution('(abasdc)()()()'))
from collections import deque

if __name__ == "__main__":
    dq = deque()
    dq.append(1)
    print(dq)

    dq.append(2)
    print(dq)

    dq.appendleft(0)
    print(dq)

    dq.pop()
    print(dq)
    
    dq.popleft()
    print(dq)

"""
매일 온도를 나타내는 int형 배열 temperatures 가 주어진다. 
answer 배열의 원소 asnwer[i]는 i번째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
만약 더 따뜻해지는 날이 없다면 answer[i]==0이다. answer배열을 반환하는 함수를 구현하시오.

input: temperatures = [73,74,75,71,69,72,76,73]
output: [1,1,4,2,1,1,0,0]

input = [100, 2,5,7,1,29,5,21,6,11]
output = [0,1,1,2,1,0,1,0,1,0] 
Brute Force method:
returnval = []
1. for i in range(length(temperatures)):
        for j in range(i+1,len(temperatures)):
            if temperatures[j] > temperatures[i]:
                returnval.append(j-i)
            else:   
                pass
        returnval.append(0)
return returnval

Stack method
1. create a stack
2. loop through temperatures
3. if new temp is larger than top of stack, keep popping.
4. Once popped, collect 
4. Else, stack.
5. Case stack is not empty, remove all.


Dummy code:
ans = [0] *len(temperatures)
# if length(temperatures) == 1 or length(temperatures)==0: return [0]

# for curr_day, curr_temp in enumerate(temperatures):
    while stack and stack.top() < current_temp:
        prev_day,_ = stack.pop 
        ans[prev_day] = curr_day - prev_day
    stack.append((curr_day,curr_temp))
return ans
        
"""

def dailyTemperatures(temperatures):
    if len(temperatures) == 0  or len(temperatures) == 1:
        return [0]
    
    stack = []
    ans = [0] * len(temperatures)
    for curr_day, curr_temp in enumerate(temperatures):
        while stack and stack[-1][1] < curr_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = curr_day - prev_day
        stack.append((curr_day, curr_temp))
    return ans
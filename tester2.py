def solution(numbers, target):
    def helper(numbers, target, index, path):
        if index == len(numbers):
            if path == target:
                return 1
            return 0
        

        counter = 0
        counter += helper(numbers, target, index+1, path+numbers[index])
        counter += helper(numbers, target, index+1, path-numbers[index])
        
        return counter
    
    return helper(numbers, target, 0,0)

if __name__ == "__main__":
    print(solution([1,1,1,1,1], 3))
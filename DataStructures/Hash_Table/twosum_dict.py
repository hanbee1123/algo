"""
문제: 
정수가 저장된 배열 nums가 주어졌을 때, nums의 원소중 두 숫자를 더해서 target이 될 수 있으면 True, 
불가능 하면 False를 반환하세요. 
같은 원소를 두번 사용할 수 없습니다.

문제접근법:
- nums를 loop한다.
- target - nums가 dictionary에 있는지 확인한다.
- 만약 없으면, dictionary에 target - nums를 key로, nums값을 value로 넣는다.
- 만약 있으면, 우리는 답은 찾은 것이다. return True 

"""

def twosum(nums, target):
    #dictionary should have {val:index}
    dictionary = {}
    for i in range(len(nums)):
        if target - nums[i] in dictionary:
            return (dictionary[target-nums[i]], i)
        else:
            dictionary[nums[i]] = i

if __name__ == "__main__":
    twosum([2,7,11,15], 9)
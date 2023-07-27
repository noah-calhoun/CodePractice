
def twoSum(nums, target):
    memo = {}

    for i, num in enumerate(nums):
        needed = target - num
        if needed in memo:
            return [i, memo.get(needed)]
        
        else:
            memo[num] = i

    return








if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
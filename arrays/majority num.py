

def majorityElement(nums):
    memo = {}

    for num in nums:
        if num in memo:
            memo[num] = memo.get(num) + 1
        else:
            memo[num] = 1

    return max(memo, key=memo.get)



if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))
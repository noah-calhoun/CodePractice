
def twoSum(nums, target):
    p1 = 0
    p2 = len(nums) -1
    while p1 < p2:
        curSum = nums[p1] + nums[p2]
        if curSum > target:
            p2 -= 1      
        elif curSum < target:
            p1 += 1
        else:
            return [p1+1, p2+1]




def twoSumold(numbers, target):
    p1 = 0
    p2 = 1
    if len(numbers) < 2:
        return [0,0]
    while True:
        
        attempt = numbers[p1] + numbers[p2]
        if attempt == target:
            return [p1+1, p2+1]
        
        elif attempt > target or p2 == len(numbers) - 1:
            p1 += 1
            p2 = p1 + 1
        
        else:
            p2 += 1




if __name__ == '__main__':
    numbers = [2,7,11,15]
    # numbers = [-1,0]
    target = 18

    print(twoSum(numbers, target))

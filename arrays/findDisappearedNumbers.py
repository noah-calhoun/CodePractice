# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.


def findDisappearedNumbers(nums):
    n = len(nums)
    res = []
    for i in range(1, n+1): 
        res.append(i)

    for val in nums:
        if val in res:
            res.remove(val)
    return res





if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    findDisappearedNumbers(nums)
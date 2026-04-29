# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


from typing import List


def findMinOld(nums):
    small = nums[0]
    left, right  = 0, len(nums) - 1
    mid = (right + left) //2

    while left <= right:
        if nums[left] < nums[right]:
            small = min(nums[left], small)
            break
        
        small = min(small, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (right + left) //2

    return small



def findMin(nums: List[int]) -> int:
        # 3, 4, 5, 6, 1, 2        
        l, r = 0, len(nums) - 1
        minVal = nums[0]
        while l < r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break
            mid = (r + l) // 2
            minVal = min(minVal, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return minVal


if __name__ == '__main__':
    nums = [3,4,5,6,1,2]
    # nums = [4,5,6,7,0,1,2]
    nums = [2,1]
    # nums = [4,5,6,7]

    findMin(nums)
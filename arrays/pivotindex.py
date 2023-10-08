# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, val in enumerate(nums):
        total -= val
        if left == total:
            return i
        left += val
    return -1

def pivotIndex2(nums):

    #binary search, take middle, find total of each side, move in either direction
    # DO NOT include mid point in calculation of total
    if len(nums) < 3:
        return -1
    mid = len(nums) // 2
    left = sum(nums[:mid]) 
    right = sum(nums[mid+1:])

    while mid > 0 and mid < len(nums)-1:
        if left == right:
            return mid

        if left > right:
            left -= nums[mid - 1]
            right += nums[mid]
            mid -= 1
        else:
            left += nums[mid]
            right -= nums[mid + 1]
            mid += 1

    if mid == 0 and right == 0:
        return 0
    elif mid == len(nums) - 1 and left == 0:
        return mid

    return -1 if left != right else mid



def pivotIndex1(nums):
    # iterate through list, calculating total of all to left. do it again for right, find where ==
    # 2*n, which is... okay i think?
    # Brute Force
    leftTotal = 0
    rightTotal = 0
    left = []
    right = []
    for val in nums:
        leftTotal += val
        left.append(leftTotal)
    for val in reversed(nums):
        rightTotal += val
        right.append(rightTotal)

    for item in right:
        if left.index(item):
            return left.index(item)
    return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    # nums = [2, 3, 1, 0, 6]
    # nums = [-1,-1,-1,-1,-1,0]
    
    print(pivotIndex(nums))
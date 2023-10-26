# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i, l, r = 0, 0, len(nums) -1
    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1

        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
            continue
        i += 1
    
    return


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    # nums = [2,1]
    # nums = [1,2,0]
    sortColors(nums)
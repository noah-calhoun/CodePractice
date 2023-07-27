# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
#   and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
def threeSum(nums):
    output = []
    nums.sort()
    
    for i, value in enumerate(nums):
        left, right = i+1, len(nums)-1
        # list is sorted, value can never be == 0 
        if value > 0:
            break
        if i > 0 and value == nums[i - 1]:
            continue

        while left < right:
            sum3 = nums[left] + nums[right] + value
            if sum3 > 0:
                right -= 1
            elif sum3 < 0:
                left += 1
            else:
                new = [nums[left], value, nums[right]]
                if new not in output:
                    output.append([nums[left], value, nums[right]])
                left += 1
                right -= 1
                    
    return output






# O(n^3) Very bad, but also a bruteforce
def threeSumBrute(nums):
    i = 0
    j = 1
    k = 2
    output = []    
    if len(nums) == 3 and nums[i] + nums[j] + nums[k] == 0:
        output.append([nums[i], nums[j], nums[k]])
        return output
    while i < len(nums) - 3:
        if nums[i] + nums[j] + nums[k] == 0:
            new = [nums[i], nums[j], nums[k]]
            new.sort()
            
            if new not in output:
                output.append(new)
        if k < len(nums)-1:
            k += 1
        elif j < k -1:
            j += 1
            k = j + 1
        elif i < j -1:
            i += 1
            j = i + 1
            k = j + 1

    return output



if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    # nums = [0,0,0]
    print(threeSum(nums))

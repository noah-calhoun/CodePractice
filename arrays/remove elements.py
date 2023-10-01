
def removeElement(nums, val):
    left = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[left] = nums[i]
            left +=1           

    return left



def removeElement1(nums, val):
    """ modify in place, remove all val"""
    left = 0
    right = 0
    while right < len(nums):
        if nums[left] == None and nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            right +=1
            left += 1

        elif nums[left] == val:
            nums[left] = None
            right += 1
        
        elif nums[right] == val:
            nums[right] = None
            right +=1
        else:
            right +=1
        

    return left




if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    removeElement(nums, val)
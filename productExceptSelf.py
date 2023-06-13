# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].


def productExceptSelf(nums):
    output = [1] * len(nums)
    prefix = 1
    postfix = 1
    # prefix loop
    for i in range(len(nums)):
        num = nums[i]
        output[i] *= prefix
        prefix *= num

    # postfix loop
    for i in range(len(nums) -1, -1, -1):
        num = nums[i]
        output[i] *= postfix
        postfix *= num

    return output



if __name__ == '__main__':
    nums = [1,2,3,4]
    # k = 2
    print(productExceptSelf(nums))
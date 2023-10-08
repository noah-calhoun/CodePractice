
def nextGreaterElement(nums1, nums2):
    out = []
    memo = {}
    stack = []
    for num in nums2:
        # If the stack is not empty and the current number is greater than the number at the top of the stack
        while stack and num > stack[-1]:
            # Pop the top element from the stack and store the current number as its next greater element in the memo dictionary
            memo[stack.pop()] = num
        # Push the current number onto the stack
        stack.append(num)
    
    # Iterate through nums1 and look up the next greater element in the memo dictionary
    # Use -1 as the default value if the element is not found
    for num in nums1:
        out.append(memo.get(num, -1))
        
    return out


def nextGreaterElement1(nums1, nums2):
    out = []
    memo = {}
    right = None
    # map vals of nums2, later iterate through nums1
    for j, val in reversed(list(enumerate((nums2)))):
        
        if j < len(nums2)-1 and nums2[j+1] > val:
            memo[val] = nums2[j+1]
            right = nums2[j+1]

        elif right and right > val:
            memo[val] = right
        else:
            memo[val] = -1
    
    for item in nums1:
        out.append(memo.get(item))
        
    return out






if __name__ == '__main__':
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    print(nextGreaterElement(nums1, nums2))
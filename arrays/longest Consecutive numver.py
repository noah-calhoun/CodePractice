# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


def longestConsecutive(nums):
    memo = set(nums).sorted()
    largest = 1

    for num in nums:
        if num + 1 in memo:
            largest += 1    
        else:
            largest = 0
    return largest









if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    
    print(longestConsecutive(nums))
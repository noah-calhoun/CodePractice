# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestConsec(nums):
    memo = set(nums)
    total = 0
    if len(nums) == 0:
        return total
    
    for num in memo:

        if num -1 in memo:
            cur_num = num            
            cur_streak = 1
            while cur_num in memo:
                cur_streak += 1
                cur_num += 1
            total = max(total, cur_streak)

    
    return total

def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak









if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    nums = [0]
    print(longestConsecutive(nums))
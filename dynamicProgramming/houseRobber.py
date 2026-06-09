from typing import List

# You are a robber planning to rob houses along a street. 
# Each house has some amount of money. The constraint: you cannot rob two adjacent houses (the alarm will trigger).

# Given an integer array nums where nums[i] is the amount of money in house i, 
# return the maximum amount of money you can rob without alerting the police.

# Examples:
# Input:  [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 0 (1) + house 2 (3) = 4

# Input:  [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Rob house 0 (2) + house 2 (9) + house 4 (1) = 12
# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

def rob(nums: List[int]) -> int:
    memo = {}

    
    pass


# Tests
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([0], 0),
        ([1, 2], 2),
        ([2, 1, 1, 2], 4),
    ]

    for nums, expected in tests:
        result = rob(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | rob({nums}) = {result} (expected {expected})")

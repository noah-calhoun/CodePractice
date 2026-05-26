

from typing import List


def singleNumber( nums: List[int]) -> int:
    # a ^ a ^ b = b
    res = 0
    for val in nums:
        res = res ^ val
    return res

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    singleNumber(nums)

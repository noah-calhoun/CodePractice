import math
from typing import List


def countBeautifulPairs(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            firstDigit = int(str(nums[i])[0])
            lastDigit = int(str(nums[j])[-1])
            if math.gcd(firstDigit, lastDigit) == 1:
                result += 1
    return result

if __name__ == '__main__':
    nums = [2,5,1,4]
    print(countBeautifulPairs(nums))
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         itemDict = {}
#         for item in nums:
#             if item in itemDict.keys():
#                 return True
#             else:
#                 itemDict[item] = item
#         return False

# O(nlogn)
def containsDuplicateSort(nums):
    nums.sort()
    for i in range(len(nums)):
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            return True

    return False


if __name__ == '__main__':
    print(containsDuplicateSort([1,2,3,4,5]))
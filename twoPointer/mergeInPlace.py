

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i, j = 0, 0
    while i < len(nums1) and m >= 0 and n >= 0:
        # Swap num
        if nums2[j] < nums1[i]:
            # temp = nums1[i]
            # nums1[i] = nums2[j]
            # nums2[j] = temp
            nums1[i], nums2[j] = nums2[j], nums1[i]
        elif nums1[i] == 0:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i += 1
            j += 1
        else:
            i += 1
        if j+1 <= n and  nums2[j] > nums2[j+1]:
                nums2[j], nums2[j+1] = nums2[j+1], nums2[j]

if __name__ == '__main__':
    # nums1 = [1,2,3,0,0,0] 
    nums1 = [4,5,6,0,0,0]
    m = 3
    # nums2 = [2,5,6]
    nums2 = [1,2,3]
    n = 3
    merge(nums1, m, nums2, n)



from ast import List


def singleNumber(nums):
    res = 0
    for n in nums:
        res = res ^ n
    return res






if __name__ == '__main__':
    l1 = [4,1,2,1,2]
    singleNumber(l1)
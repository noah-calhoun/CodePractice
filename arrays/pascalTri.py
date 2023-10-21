# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def generate(n):

    res = []
    for i in range(n):
        arr = []
        if i == 0:
            arr.append(1)
        for j in range(i):
            if i-1 > len(res) - 1:
                arr[i] = res[i-1] + res[i]
            else:
                arr.append(1)
        res.append(arr)

    return res





if __name__ == '__main__':
    n = 5
    generate(n)
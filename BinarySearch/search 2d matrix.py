# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


from typing import List


def searchMatrixOld(matrix, target):
    pointVert = 0
    pointHorz = 0

    while True:
        # check vert
        # checkdown = matrix[pointVert + 1][pointHorz]
        # checkright = matrix[pointVert][pointHorz + 1]
        current = matrix[pointVert][pointHorz]
        lengthVert = len(matrix) > pointVert + 1
        lengthHorz = len(matrix[0]) > pointHorz + 1

        if matrix[pointVert][pointHorz] == target:
            return True
        
        elif lengthVert and matrix[pointVert + 1][pointHorz] <= target:
            pointVert += 1

        elif lengthHorz and matrix[pointVert][pointHorz + 1] >= target:
            pointHorz += 1

        elif lengthVert and matrix[pointVert + 1][pointHorz] <= current:
            pointVert += 1

        elif lengthHorz and matrix[pointVert][pointHorz + 1] >= current:
            pointHorz += 1

        else:
            return False
        



def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        row, rowL, rowR = 0, 0, len(matrix[0]) -1
        # Find the row, then the column, then binary search value
        while row < len(matrix) - 1:
            leftVal, rightVal = matrix[row][rowL], matrix[row][rowR]
            if (target >= leftVal) and (target <= rightVal):
                # row found, break
                break 
            row += 1
        while rowL <= rowR:
            mid = (rowL + rowR) // 2
            value = matrix[row][mid]
            if target == value:
                return True
            elif target > matrix[row][mid]:
                rowL = mid + 1
            else:
                rowR = mid - 1

        return False



if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix =  [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    # matrix = [[1,3]]
    # matrix = [[1,3,5]]
    # target = 6
    target = 10

    print(searchMatrix( matrix, target))
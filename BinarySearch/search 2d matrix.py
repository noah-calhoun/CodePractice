# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


def searchMatrix(matrix, target):
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
        







if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix = [[1,3]]
    matrix = [[1,3,5]]
    target = 6

    print(searchMatrix(matrix, target))
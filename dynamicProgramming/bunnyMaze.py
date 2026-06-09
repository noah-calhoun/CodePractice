"""
Bunny Maze DP Problem

Problem: Find a path for a bunny through a maze using dynamic programming.
"""


def solve_bunny_maze(n,m):
    memo = {}
    for i in range(1, n + 1 ):
        memo[(i,1)] = 1
    for j in range(1, m + 1 ):
        memo[(1, j)] = 1

    for i in range(2, n+1):
        for j in range(2, m+1):
            memo[(i, j)] = memo[(i-1, j)] + memo[(i, j-1)]
    
    return memo[(n,m)]
    
    # TODO: Initialize DP table
    
    # TODO: Set base case
    
    # TODO: Fill DP table
    
    # TODO: Return result
    pass


if __name__ == "__main__":
    # Test cases
    print(solve_bunny_maze(5,4))
    pass

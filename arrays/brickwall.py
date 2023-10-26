# There is a rectangular brick wall in front of you with n rows of bricks. 
# The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.
# Draw a vertical line from the top to the bottom and cross the least bricks. 
# If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, 
# in which case the line will obviously cross no bricks.
# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

def leastBricks2(wall):
    countGap = { 0 : 0 }    # { Position : Gap count }
    for r in wall:
        total = 0   # Position
        for b in r[:-1]:
            total += b
            countGap[total] = 1 + countGap.get(total, 0)

    return len(wall) - max(countGap.values())


def leastBricks(wall):
    memo = {0:0}
    for i in range(len(wall)):
        dist = 0
        for j in range(len(wall[i])-1):
            dist += wall[i][j]
            memo[dist] = 1+ memo.get(dist, 0)

    
    return  abs(len(wall) - max(memo.values()))




if __name__ == '__main__':

    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    # wall = [[1],[1],[1]]
    print(leastBricks(wall))
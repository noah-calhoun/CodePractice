# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

def maxArea(heights):
    maxCap = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        height = min(heights[left], heights[right])
        length = right - left
        capacity = height * length
        if capacity > maxCap:
            maxCap = capacity
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return maxCap













if __name__ == '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
    print(maxArea(heights))


def trap(height):
        # volume = least height * distance of bars
        # go across each row, calc volume, then move to next height level
        volume = 0
        for i in range(len(height)-1):
            if  i - 1 >= 0 and i + 1 < (len(height)-1):
                rain = min([height[i-1], height[i+1]]) - height[i]
                if rain > 0:
                    volume += rain
        return volume


if __name__ == '__main__':
    height = [0,2,0,3,1,0,1,3,2,1]

    print(trap(height))
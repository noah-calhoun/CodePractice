# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] 
# is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


def dailyTemperatures(temps):
    stack = []
    out = [0]*len(temps)

    for i, val in enumerate(temps):
        while stack and val > stack[-1][0]:
            ignore, stack_Index = stack.pop()
            out[stack_Index] = i - stack_Index
        stack.append((val, i))

    return out



if __name__ == '__main__':
    temps = [73,74,75,71,69,72,76,73]
    dailyTemperatures(temps)
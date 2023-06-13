from heapq import heapify


def replaceElements(arr):
    max = arr[0]
    maxIndex = 0
    output = []
    for i, num in enumerate(arr):
        # Search through array for new max
        if maxIndex == i:
            if i < len(arr)-1:
                max = arr[i + 1]
                for j, newNum in enumerate(arr):
                    if j <= i:
                        continue
                    if newNum >= max:
                        max = newNum
                        maxIndex = j
        output.append(max)
    output[len(arr)-1] = -1 

    return output



if __name__ == '__main__':
    arr = [17,18,5,4,6,1]
    print(replaceElements(arr))
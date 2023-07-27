
def getConcatenation(arr):
    for i in range(len(arr)):
        arr.append(arr[i])
    return arr


if __name__ == '__main__':
    arr = [1,2,3,1]
    print(getConcatenation(arr))
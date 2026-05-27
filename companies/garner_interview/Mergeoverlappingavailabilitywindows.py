


def mergewindow (windows):
    if not windows:
        return []
    
    windows.sort(key=lambda x: x[0])
    result = [windows[0][:]]          # seed with the first window
    for start, end in windows[1:]:    # one pointer, walking forward
        last_end = result[-1][1]
        if start <= last_end:         # overlaps or touches the open window
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


if __name__ == "__main__":
    windows = [[60,120],[100,150],[200,240],[150,180]]
    # windows = [[60,120],[100,150],[150,180],[200,240],]
    # Output: [[60,180],[200,240]]
    print(mergewindow(windows))
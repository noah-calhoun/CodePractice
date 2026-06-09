
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        window = [intervals[0]]
        current = 0
        for interval in intervals:
            if interval == window[current]:
                 continue
            if interval[0] <= window[current][1]:
                window[current][1] = max(interval[1], window[current][1])
            else:
                window.append(interval)
                current += 1
        return window

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))
from hashlib import new


class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pairs = self.items.get(key, None)
        if not pairs:
            self.items[key] = [[value, timestamp]]
        else:
            pairs.append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        items = self.items.get(key)
        l, r = 0, len(items) - 1
        while l <= r:
            m = (l + r) // 2
            check = items[m][1]
            if check <= timestamp:
                res = items[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1);  #// store the key "alice" and value "happy" along with timestamp = 1.
    # timeMap.set("alice", "sad", 3);    #// store the key "alice" and value "sad" along with timestamp = 3.

    timeMap.get("alice", 1);           #// return "happy"
    timeMap.get("alice", 2);           #// return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp
    timeMap.set("alice", "sad", 3);    #// store the key "alice" and value "sad" along with timestamp = 3.1.
    timeMap.get("alice", 3);           #// return "sad"
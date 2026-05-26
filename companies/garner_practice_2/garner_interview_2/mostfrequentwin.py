# You're building a feature for a user activity dashboard. 
# Given a list of user action logs, each with a timestamp and an action string, 
# return the top K most frequent actions within the last window seconds relative to the most recent timestamp in the list.

def most_frequent_window(logs, window_size, k):
    # first sort logs by TS
    logs.sort(key=lambda x: x['timestamp'])
    maxs = {}
    windowVals = {}
    l = 0 
    r = 0
    while r < len(logs):
        raction = logs[r]['action']
        laction = logs[l]['action']

        if r == window_size:
            # remove value at L, add val at R
            windowVals[laction] =  windowVals.get(laction, 0) - 1
            windowVals[raction] =  windowVals.get(laction, 0) + 1
            
            maxs[raction] = max(windowVals[raction],  maxs[raction])
            r += 1
            l += 1
        else:
            # add val at R
            windowVals[raction] =  windowVals.get(laction, 0) + 1
            maxVal = maxs.get(raction, 0)
            maxs[raction] = max(windowVals[raction],  maxVal)
            r += 1
    top_k = sorted(maxs, key=maxs.get, reverse=True)[:k]
    return top_k

if __name__ == "__main__":
    logs = [
    {'timestamp': 1, 'action': "click"},
    {'timestamp': 2, 'action': "scroll"},
    {'timestamp': 3, 'action': "click"},
    {'timestamp': 4, 'action': "click"},
    {'timestamp': 5, 'action': "scroll"},
    ]
    window = 4 
    k = 2
    print(most_frequent_window(logs, window, k))
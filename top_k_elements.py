# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
        output = []
        m = {}
        # append items to a hash, return the top/max k values
        for n in nums:
            if n in m:
                m[n] = m[n] + 1
            else:
                m[n] = 1
        
        while k != 0:
            key = max(m, key=m.get)
            output.append(key)
            k -= 1
            m[key] = 0
            
        return output

def topFreqBetter(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1,1,1,1,1,1,1,1,2,2,3,9,16]
    k = 2
    print(topFreqBetter(nums, k))
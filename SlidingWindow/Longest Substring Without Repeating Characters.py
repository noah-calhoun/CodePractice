# Given a string s, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstringOld2(s):
    charSet = set()
    windowSize = 0
    largest = 0
    for i in range(len(s)):
        
        while s[i] in charSet:
            charSet.remove(s[windowSize])
            windowSize += 1

        charSet.add(s[i])
        largest = max(largest, len(charSet))


    return largest




def lengthOfLongestSubstring(s: str) -> int:
    l, r = 0, 1
    res = min(1, len(s))
    # z x y z x y z
    # 0 1 2 3 4 5 6
    while r < len(s):
        word = s[l:r]
        char = s[r]
        if char not in word:
            res = max(res, len(word) + 1)
            r += 1
        else:
            l += 1

    return res





def lengthOfLongestSubstringOld(s):
    refDict = {}
    largest = 0
    current = 0
    for char in s:
        if char not in refDict:
            refDict[char] = 1
            current += 1
        else:
            refDict = {}
            largest = max(current, largest)
            refDict[char] = 1
            current = 1
    largest = max(current, largest)
    return largest




if __name__ == '__main__':
    s = "abcabcbb"
    s = "pwwkew"
    # s = "dvdf"
    print(lengthOfLongestSubstring(s))
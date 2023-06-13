
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    stringS = {}
    # Build out hash with char as keys and count as value
    for char in s:
        if char in stringS.keys():
            stringS.update({char: stringS[char] + 1})
        else:
            stringS[char] = 1

    # Check each letter of string t, decrementing value on each occurence
    for charT in t:
        if charT in stringS.keys() and stringS[charT] > 0:
            stringS.update({charT: stringS[charT] - 1})
        else:
            return False
        
    return True


def isAnagramSort(s, t):
    return s.sorted() == t.sorted()



        memo = {}
        for i, num in enumerate(nums):
            value = target - num
            # Check map for previous calculation
            if value in memo:
                return [i, memo[value]] 
            
            # If not found, and not in map, add value to map
            memo[num] = i



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    s = "ab"
    t = "a"
    print(isAnagram(s, t))
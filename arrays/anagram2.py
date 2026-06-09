
def isAnagram(s, t):
    sDict = {}
    tDict = {}
    i = 0
    for i in range(len(s)):
        sDict[s[i]] = sDict.get(s[i], 0) + 1
        tDict[t[i]] = tDict.get(t[i], 0) + 1
    return sDict == tDict

def firstnondupechar(s):
    result = ''
    for char in s:
        result = result ^ char
    
    return result[0]


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    s = "rat"
    t = "car"
    z = "aabbccdeeffghhiij"
    print(isAnagram(s,t))
    print(firstnondupechar(z))
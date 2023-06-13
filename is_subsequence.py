# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    remaining = len(s)
    indexS = 0
    for char in t:
        if remaining > 0 and char == s[indexS]:
            remaining -= 1
            indexS += 1

    return not bool(remaining)



if __name__ == '__main__':
    s = "abc" 
    t = "ahbgdc"
    print(isSubsequence(s, t))
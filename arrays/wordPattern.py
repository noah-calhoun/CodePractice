
# https://leetcode.com/problems/word-pattern/
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


def wordPattern(pattern, s):
    memo = {}
    res = []
    # append set to memo with pat and s?
    s = s.split(" ")
    if len(s) != len(pattern):
        return False
    for i in range(len(pattern)):
        pat = pattern[i] 
        strItem = s[i]

        if pat in memo and memo[pat] != strItem:
            return False

        elif strItem in memo.values():
            if strItem != memo.get(pat, 0):
                return False
        else:
            memo[pat] = strItem

    return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    pattern = "abba"
    s = "dog dog dog dog"
    print(wordPattern(pattern, s))

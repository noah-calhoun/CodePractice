

"longest prefix amoung all words"


def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    first_str = strs[0]
    last_str = strs[-1]
    i = 0
    while i < len(first_str) and first_str[i] == last_str[i]:
        i += 1

    return first_str[:i] 


def longestCommonPrefix1(s):
    prefix = {}
    longest = 0
    i = 0
    shortest = 99999
    for word in s:
        shortest = min(shortest, len(word))
    word = "word"
    w = word[0]
    while i < shortest:
        current = 0
        for word in s:
            if current == 0:
                current = word[i]
            elif current != word[i]:
                longest = len(prefix)
                prefix = {}
                break
            else:
                prefix[i] = current
        i += 1


    return longest









if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    
    print(longestCommonPrefix(strs))


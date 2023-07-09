# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from ast import List
import collections


def groupAnagrams(strs):
    # Method: Loop through with two for loops, append anagrams to output set, remove from loop.
    memo = {}
    for word in strs:
        temp = ""
        temp = temp.join(sorted(word))
        if temp in memo:
            memo[temp].append(word)
        else:
            memo[temp] = [word]

    return
        

def groupAnagrams1(strs):

    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

def groupAnagrams2(strs):
        # Create a dictionary to act as hashmap
        res = {}
        for word in strs:
            # We want to retain the original word to add to the dictionary
            # Therefore, create a temporary variable with the sorted word
            temp = ''.join(sorted(word))
            # If the sorted word exists in the dictionary, 
            # append to the values list
            if temp in res:
                res[temp].append(word)
            # Else, add a new key-value pair to the dictionary
            else:
                res[temp] = [word]
        # We only require the values list to be returned
        return res.values()




if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = ["",""]
    print(groupAnagrams(strs))




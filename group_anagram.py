# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from ast import List
import collections


def groupAnagrams(strs):
    # Method: Loop through with two for loops, append anagrams to output set, remove from loop.
    output = []
    output_ref = 0
    nested_output = []
    word_map = {}
    i = 0
    j = 0
    

    while True:
        if i >= len(strs):
            return output
        
        word = strs[i]
        # create hash
        if strs[i] == None:
            i += 1
            j = i
            continue
        if i == j:
            if len(word) == 0:
                nested_output.append(word)
                j += 1
                count = 0
                continue

            count = 0
            for char in word:
                count += 1
                if word_map.get(char):
                    word_map.update({char:word_map.get(char) + 1})
                else:
                    word_map.update({char:1})
            j += 1
            nested_output.append(word)

        # point to next word, search chars
        elif j <= len(strs) - 1:
            next_word = strs[j]
            char_count = 0
            if next_word == None:
                j += 1
                continue
            for char in next_word:
                
                if word_map.get(char) and word_map.get(char) > 0:
                    # inc count and map
                    char_count += 1
                else:
                    break
            if count == char_count:
                nested_output.append(next_word)
                strs[j] = None

            j += 1
            

        elif i  < len(strs):
            i += 1
            j = i
            output.append(nested_output)
            nested_output = []
            word_map = {}

        
        else:
            return output
        

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
    print(groupAnagrams2(strs))




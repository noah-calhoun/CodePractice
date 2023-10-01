# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.



def checkInclusion( s1: str, s2: str):
        window = 0
        stringBox = {}
        if len(s1) <= len(s2):
            string1 = s1
            string2 = s2
        else:
            string1 = s2
            string2 = s1

        for char in s1:
            if char in stringBox:
                stringBox[char] += 1
            else:
                stringBox[char] = 1

        while window < len(string2):
            box = {}
            for i in range(window, window + len(string1)):
                if i >= len(string2):
                    return False
                char = string2[i]
                if char in box:
                    box[char] += 1
                else:
                    box[char] = 1
                
            if box == stringBox:
                return True
            
            else:
                window += 1

        return False



if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s2 = "eidboaoo"
    checkInclusion(s1, s2)
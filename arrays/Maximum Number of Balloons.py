# https://leetcode.com/problems/maximum-number-of-balloons/
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text: str) -> int:
    from collections import Counter
    
    counts = Counter(text)
    counts['l'] //= 2
    counts['o'] //= 2
    
    return min(counts['b'], counts['a'], counts['l'], counts['o'], counts['n'])



def maxNumberOfBalloons1(text):
    out = 0
    current = "balloon"

    for char in text:
        if char in current:
            current = current.replace(char, "", 1)
        if current == "":
            current = "balloon"
            out +=1

    return out









if __name__ == '__main__':
    text = "loonbalxballpoon"
    maxNumberOfBalloons(text)






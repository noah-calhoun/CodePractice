# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

def isPalindrome(s):
    # remove bad characters
    # s = s.replace(" ", "").replace(",","").replace(":","").lower()
    s = s.lower()
    s = remove_special_characters(s)
    p1 = 0
    p2 = len(s) - 1
    if len(s) // 2 == 0:
        length = int((len(s) - 1) / 2)
    else:
        length = int((len(s)) / 2)
    for i in range(length):
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True


def remove_special_characters(s):
    special_chars = "!@#$%^&*()_+=-[]{}|\\;:'\"<>,./?"
    clean_s = ""
    for char in s:
        if char.isalnum():
            clean_s += char
    return clean_s



if __name__ == '__main__':
    # strs = ["eat","tea","tan","ate","nat","bat"]
    s = "A man, a plan, a canal: Panama"
    # strs = ["",""]
    print(isPalindrome(s))

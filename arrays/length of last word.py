

def lengthOfLastWord(s):
    if not words:
        return 0
    words = s.split()
    return len(words[-1])







if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    
    print(lengthOfLastWord(s))
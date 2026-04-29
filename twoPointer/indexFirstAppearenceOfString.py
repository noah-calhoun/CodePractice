


def strStr(haystack: str, needle: str) -> int:
        
        # s a d b u t s a d
        # 1 2 3 4 5 6 7 8 9
        need = len(needle)
        for i in range(len(haystack) - need + 1):
              if haystack[i:i+need] == needle:
                return i
              
        return -1



if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    haystack = "mississippi" 
    needle = "issip"
    
    print(strStr(haystack, needle))

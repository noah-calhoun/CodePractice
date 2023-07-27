# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    closeToOpen = {")":"(", "}":"{", "]":"["}
    stack = []

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if not stack:
        return True
    else:
        return False

def isValidOld(s):

    
    data = {"(":0,")":0, "{":0, "}":0, "[":0, "]":0}

    for char in s:
        data[char] = data.get(char, 0) + 1

    if data.get('[') == data.get(']') and data.get('{') == data.get('}') and data.get('(') == data.get(')'):
        return True
    return False



if __name__ == '__main__':
    s = "([)]"
    s = "()[]{}"
    s = "([{}{}])"
    # s = "()()"
    print(isValid(s))
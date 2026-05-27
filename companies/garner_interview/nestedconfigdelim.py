
def nested_config_delimiter(config):
    stack = []
    closeToOpen = {")":"(", "}":"{", "]":"["}
    openers = set(closeToOpen.values())

    # validChars = ['(', ')', '[', ']', '{', '}']

    for char in config:
        if char not in openers:
            continue
        if char in closeToOpen:
            if stack and closeToOpen[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack

if __name__ == "__main__":
    config = "a(b[c]{d})"
    print(nested_config_delimiter(config))
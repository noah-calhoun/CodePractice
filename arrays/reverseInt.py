
def reverse(x: int) -> int:
        hold = []
        output = ''
        length = len(str(x))
        for i in range(length):
            hold.append(x % 10)
            x = x // 10
        print(hold)
        for item in hold:
            output += str(item)
        return int(output)

if __name__ == '__main__':
    x = 123
    print(reverse(x))
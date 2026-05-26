from typing import List


def plusOne(digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            #Initial value 
            if i == len(digits)-1:
                digits[i] += 1
            if digits[i] == 10 and i != 0:
                digits[i] = 0
                digits[i-1] = digits[i-1] + 1
        if digits[0] == 10:
            output = []
            for val in digits:
                if val == 10:
                    output.append(1)
                    output.append(0)
                else:
                    output.append(val)
            return output
        else:
            return digits
                


if __name__ == '__main__':
    digits = [4,3,2,1]
    digits = [9,9,9,9]
    print(plusOne(digits))
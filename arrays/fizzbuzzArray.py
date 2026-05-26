
from typing import List


def fizzBuzz( n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            item = ""
            if i % 3 == 0:
                item += "Fizz"
            if i % 5 == 0:
                item += "Buzz"
            if item:
                result.append(item)
            else:
                result.append(str(i))
        return result

if __name__ == "__main__":
    n = 5
    print(fizzBuzz(n))
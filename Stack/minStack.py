# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.


class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None
        self.minValueIndex = None
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minValue == None or self.minValue > val:
            self.minValue = val
            # maybe handle min index here
        return

    def pop(self) -> None:
        out = self.stack.pop()
        if out == self.minValue:
            minVal = None
            for val in self.stack:
                if minVal == None or val < minVal:
                    minVal = val

            self.minValue = minVal
        return


    def top(self) -> int:
        out = self.stack[len(self.stack) - 1]
        return out        

    def getMin(self) -> int:
        return self.minValue
    


if __name__ == '__main__':
    obj = MinStack()
    obj.push(5)
    obj.push(4)
    obj.push(6)
    obj.push(1)
    obj.push(8)
    obj.push(0)
    obj.pop()
    param_3 = obj.top()
    print(obj.getMin())
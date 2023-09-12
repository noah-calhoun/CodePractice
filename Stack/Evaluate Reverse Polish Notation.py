# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul
}


def evalRPN(input):
    stack = []
    operator = ["*","+","-"]

    for val in input:
        if val == "/":
            item1 = int(stack.pop())
            item2 = int(stack.pop())
            total = int(float(item2) / item1)
            stack.append(total)

        elif val in operator:
            item1 = int(stack.pop())
            item2 = int(stack.pop())
            total = (ops[val](item2, item1))
            stack.append(total)
        else:
            stack.append(val)

    return int(stack[0])


if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # tokens = ["4","13","5","/","+"]
    # tokens = ["18"]
    print(evalRPN(tokens))

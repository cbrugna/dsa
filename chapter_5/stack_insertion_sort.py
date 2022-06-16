# Insertion sort using stacks

from turtle import clear


def iss(stack):
    tempStack = []
    topInputStack = None
    while len(stack) != 0:
        topInputStack = stack.pop()
        while len(tempStack) != 0 and tempStack[-1] > topInputStack:
            stack.append(tempStack.pop())
        tempStack.append(topInputStack)
    return tempStack

if __name__ == "__main__":
    stack = [8, 1, 2]
    print(stack)
    sorted_stack = iss(stack)
    print(sorted_stack)
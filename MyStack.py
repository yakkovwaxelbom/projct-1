from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, element=None) -> bool:
        if element is not None:
            self.top += 1
            self.stack.append(element)
            return True
        return False

        #
        # """Push an element onto the stack.
        # Args:
        #     element: The element to be pushed onto the stack.
        #
        # Returns:
        #     bool: True if the element was successfully pushed, False otherwise.
        # """

    def pop(self) -> Any:
        if self.is_empty():
            return "underflow"
        else:
            self.top -= 1
            previous_top = self.stack[self.top + 1]
            del self.stack[self.top + 1]
            return previous_top

    # Return the top element from the stack without removing it
    def peek(self) -> Any:
        if self.top > -1:
            return self.stack[self.top]
        return "underflow"

    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        return False

    def size(self) -> int:

        # Returns:
        #     int: The number of elements in the stack.

        return len(self.stack)

    def clear(self) -> None:
        for i in range(len(self.stack) - 1, -1, -1):
            del self.stack[i]
        self.top = -1
        # """Remove all elements from the stack."""


# shalom = MyStack()
# # print(shalom.push())  # False
# print(shalom.push(3))  # True
# shalom.push(4)
# print(shalom.peek())  # 4
# print(shalom.pop())  # 4
# print(shalom.pop())  # 3


def check_properly_nested(string: str):
    if len(string) == 0:
        return True
    stack = MyStack()
    for char in string:
        if char in ('(', '{', '['):  # to check
            stack.push(char)
        elif char == ')' and stack.peek() == '(':
            stack.pop()
        elif char == ']' and stack.peek() == '[':
            stack.pop()
        elif char == '}' and stack.peek() == '{':
            stack.pop()
    if stack.is_empty():
        return True
    else:
        return False


def test(func):
    legals = ['((67)[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s


test(check_properly_nested)

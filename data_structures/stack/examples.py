from stack import MyStack

# EXAMPLE: Valid Parenthesis


def isValidParenthesis(string):
    openBrackets = ["{", "(", "[", "<"]
    closeBrackets = {"}": "{", ")": "(", "]": "[", ">": "<"}
    stack = MyStack()

    for letter in string:
        if openBrackets.__contains__(letter):
            stack.push(letter)
        elif closeBrackets.keys().__contains__(letter):
            if closeBrackets[letter] != stack.pop():
                return False
        else:
            continue

    return stack.size() == 0


str = "{()}"
print("IS VALID:", str, isValidParenthesis(str))
str = "{(Rahul)}"
print("IS VALID:", str, isValidParenthesis(str))
str = "[{(Rahul)}"
print("IS VALID:", str, isValidParenthesis(str))
str = "{}"
print("IS VALID:", str, isValidParenthesis(str))

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -------------------------- Queue using Stack --------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Amortized Analysis
# Amortized analysis gives the average performance (over time) of each operation in the worst case. The basic idea is that a worst case operation can alter the state in such a way that the worst case cannot occur again for a long time, thus amortizing its cost.


class MyQueue:
    def __init__(self):
        self.queue = MyStack()
        self.temp = MyStack()
        self.front = None

    def push(self, x: int) -> None:
        if self.queue.is_empty():
            self.front = x
        self.queue.push(x)

    # Time complexity: Amortized O(1), Worst-case O(n).
    def pop(self) -> int:
        if self.temp.is_empty():
            while self.queue.size():
                self.temp.push(self.queue.pop())
        return self.temp.pop()

    def peek(self) -> int:
        if not self.temp.is_empty():
            return self.temp.peek()
        return self.front

    def empty(self) -> bool:
        return self.queue.size() == 0 and self.temp.size() == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print("POP: ", obj.pop())
print("PEEK: ", obj.peek())
# print("POP: ", obj.pop())
print("IS EMPTY?", obj.empty())

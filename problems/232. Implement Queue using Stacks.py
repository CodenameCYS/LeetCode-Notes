'''
=== 232. Implement Queue using Stacks ===

Implement the following operations of a queue using stacks.
- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

Example:
    MyQueue queue = new MyQueue();
    queue.push(1);
    queue.push(2);  
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false

Notes:
    1. You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    2. Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    3. You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''
# === 20ms(96.46%) && 12.7MB(100%) === #
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack = self.stack[::-1]
        self.stack.append(x)
        self.stack = self.stack[::-1]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
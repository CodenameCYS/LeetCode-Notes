'''
=== 622. Design Circular Queue ===

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
Implementation the MyCircularQueue class:
    - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    - int Front() Gets the front item from the queue. If the queue is empty, return -1.
    - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    - boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    - boolean isEmpty() Checks whether the circular queue is empty or not.
    - boolean isFull() Checks whether the circular queue is full or not.
 
Example 1:
    Input
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 3, true, true, true, 4]
    Explanation
    MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    myCircularQueue.enQueue(1); // return True
    myCircularQueue.enQueue(2); // return True
    myCircularQueue.enQueue(3); // return True
    myCircularQueue.enQueue(4); // return False
    myCircularQueue.Rear();     // return 3
    myCircularQueue.isFull();   // return True
    myCircularQueue.deQueue();  // return True
    myCircularQueue.enQueue(4); // return True
    myCircularQueue.Rear();     // return 4
 
Constraints:
    1. 1 <= k <= 1000
    2. 0 <= value <= 1000
    3. At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
 
- Follow up: Could you solve the problem without using the built-in queue? 
'''
# === 64ms(90.06%) && 15MB === #
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.st = 0
        self.ed = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.ed - self.st >= self.k:
            return False
        self.queue[self.ed % self.k] = value
        self.ed += 1
        return True

    def deQueue(self) -> bool:
        if self.ed <= self.st:
            return False
        self.st += 1
        return True

    def Front(self) -> int:
        if self.st >= self.ed:
            return -1
        return self.queue[self.st % self.k]

    def Rear(self) -> int:
        if self.st >= self.ed:
            return -1
        return self.queue[(self.ed-1) % self.k]

    def isEmpty(self) -> bool:
        return self.st == self.ed

    def isFull(self) -> bool:
        return self.ed-self.st == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''
=== 2336. Smallest Number in Infinite Set ===

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
    - SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    - int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    - void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 
Example 1:
    Input
    ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
    [[], [2], [], [], [], [1], [], [], []]
    Output
    [null, null, 1, 2, 3, null, 1, 4, 5]
    Explanation
    SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
    smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
    smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
    smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
    smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                       // is the smallest number, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 
Constraints:
    1. 1 <= num <= 1000
    2. At most 1000 calls will be made in total to popSmallest and addBack.
'''
# === 179ms && 14.7MB === #
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 2000)]
        
    def popSmallest(self) -> int:
        return self.nums.pop(0)

    def addBack(self, num: int) -> None:
        idx = bisect.bisect_left(self.nums, num)
        if idx >= len(self.nums) or self.nums[idx] != num:
            self.nums.insert(idx, num)
        return

# === 202ms && 14.6MB === #  
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]
        self.max_elem = 1000
        
    def popSmallest(self) -> int:
        if self.nums == []:
            self.nums = [i + self.max_elem for i in range(1, 1001)]
            self.max_elem += 1000
        return self.nums.pop(0)
        
    def addBack(self, num: int) -> None:
        while num > self.max_elem:
            self.nums.extend([i + self.max_elem for i in range(1, 1001)])
            self.max_elem += 1000
        idx = bisect.bisect_left(self.nums, num)
        if idx >= len(self.nums) or self.nums[idx] != num:
            self.nums.insert(idx, num)
        return

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
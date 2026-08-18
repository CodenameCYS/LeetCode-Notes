'''
=== 703. Kth Largest Element in a Stream ===

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:
    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note:
    1. You may assume that nums' length ≥ k-1 and k ≥ 1.
'''
import heapq
# === 784ms(14.91%) && 16.5MB(91.30%) === #
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.arr) >= self.k and val <= self.arr[-1]:
            return self.arr[-1]
        if len(self.arr) < self.k:
            self.arr.append(val)
        else:
            self.arr[-1] = val
        self.arr = sorted(self.arr, reverse=True)
        return self.arr[-1]
# === 76ms === # 网上大佬的做法
class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        self._k = k
        self._nums = nums
        heapq.heapify(self._nums)
        while len(self._nums) > self._k:
            heapq.heappop(self._nums)

    def add(self, val: int) -> int:
        if len(self._nums) < self._k:
            heapq.heappush(self._nums, val)
        elif val > self._nums[0]:
            heapq.heapreplace(self._nums, val)
        return self._nums[0]

       # Your KthLargest object will be instantiated and called as such:
       # obj = KthLargest(k, nums)
       # param_1 = obj.add(val)
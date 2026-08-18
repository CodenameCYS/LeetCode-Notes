'''
=== 384. Shuffle an Array ===

Shuffle a set of numbers without duplicates.

Example:
    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);
    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();
    // Resets the array back to its original configuration [1,2,3].
    solution.reset();
    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();
'''
from random import shuffle
# === 500ms(5.35%) && 17.9MB(100%) === # 
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.order = [i for i in range(len(nums))]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.order = [i for i in range(len(self.nums))]
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle(self.order)
        return [self.nums[i] for i in self.order]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
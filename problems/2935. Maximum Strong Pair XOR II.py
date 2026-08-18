'''
=== 2935. Maximum Strong Pair XOR II ===

You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:
    - |x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: 7
    Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
    The maximum XOR possible from these pairs is 3 XOR 4 = 7.
Example 2:
    Input: nums = [10,100]
    Output: 0
    Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
    The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.
Example 3:
    Input: nums = [500,520,2500,3000]
    Output: 1020
    Explanation: There are 6 strong pairs in the array nums: (500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) and (3000, 3000).
    The maximum XOR possible from these pairs is 500 XOR 520 = 1020 since the only other non-zero XOR value is 2500 XOR 3000 = 636.
 
Constraints:
    1. 1 <= nums.length <= 5 * 104
    2. 1 <= nums[i] <= 220 - 1
'''
# === 4674ms && 79.6MB === #
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add(self, num):
        trie = self.trie
        for digit in num:
            trie = trie.setdefault(digit, {})
        trie["eos"] = num

    def find(self, num):
        trie = self.trie
        for digit in word:
            if digit not in trie:
                return False
            trie = trie[digit]
        return "eos" in trie
    
    def find_closest(self, num):
        trie = self.trie
        for digit in num:
            if digit not in trie:
                digit = "1" if digit == "0" else "0"
            trie = trie[digit]
        return trie["eos"]
    
    def remove(self, num):
        tries = []
        trie = self.trie
        for digit in num:
            tries.insert(0, (digit, trie))
            trie = trie[digit]
        for digit, trie in tries:
            trie.pop(digit)
            if len(trie) > 0:
                break
        return
            

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def num2digit(num):
            ans = bin(num)[2:]
            return ans.rjust(20, "0")
        
        def digit2num(digits):
            ans = 0
            for digit in digits:
                ans = ans * 2 + int(digit)
            return ans
        
        def reverse(digits):
            return "".join(str(1-int(d)) for d in digits)
        
        trie = Trie()
        nums = sorted(set(nums))
        r, n = 0, len(nums)
        ans = 0
        for num in nums:
            while r < n and nums[r] <= 2 * num:
                digits = num2digit(nums[r])
                trie.add(digits)
                r += 1
            # print(r, trie.trie)
            digits = num2digit(num)
            tgt = reverse(digits)
            ret = trie.find_closest(tgt)
            ret = digit2num(ret)
            # print(num, digits, tgt, ret)
            ans = max(ans, ret^num)
            trie.remove(digits)
        # print("=" * 10)
        return ans
            
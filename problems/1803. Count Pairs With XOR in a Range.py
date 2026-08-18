'''
=== 1803. Count Pairs With XOR in a Range ===

Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.
A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

Example 1:
    Input: nums = [1,4,2,7], low = 2, high = 6
    Output: 6
    Explanation: All nice pairs (i, j) are as follows:
        - (0, 1): nums[0] XOR nums[1] = 5 
        - (0, 2): nums[0] XOR nums[2] = 3
        - (0, 3): nums[0] XOR nums[3] = 6
        - (1, 2): nums[1] XOR nums[2] = 6
        - (1, 3): nums[1] XOR nums[3] = 3
        - (2, 3): nums[2] XOR nums[3] = 5
Example 2:
    Input: nums = [9,8,4,2,1], low = 5, high = 14
    Output: 8
    Explanation: All nice pairs (i, j) are as follows:
    ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
        - (0, 3): nums[0] XOR nums[3] = 11
        - (0, 4): nums[0] XOR nums[4] = 8
        - (1, 2): nums[1] XOR nums[2] = 12
        - (1, 3): nums[1] XOR nums[3] = 10
        - (1, 4): nums[1] XOR nums[4] = 9
        - (2, 3): nums[2] XOR nums[3] = 6
        - (2, 4): nums[2] XOR nums[4] = 5
 
Constraints:
    1. 1 <= nums.length <= 2 * 104
    2. 1 <= nums[i] <= 2 * 104
    3. 1 <= low <= high <= 2 * 104
'''
# === === #
class Trie:
    def __init__(self):
        self.trie = {}
        
    def add(self, digits):        
        trie = self.trie
        for c in digits:
            if c not in trie:
                trie[c] = [0, {}]
            trie[c][0] += 1
            trie = trie[c][1]
        if "eos" not in trie:
            trie["eos"] = 1
        else:
            trie["eos"] += 1
        return
    
    def find_low(self, digits, tgt):
        trie = self.trie
        res = 0
        for d1, d2 in zip(digits, tgt):
            t = d1 ^ d2
            if d2 == 0:
                if t not in trie:
                    break
                _, trie = trie[t]
            else:
                res += trie.get(1-t, [0, {}])[0]
                _, trie = trie.get(t, [0, {}])
        res += trie.get("eos", 0)
        return res
    
    def find_high(self, digits, tgt):
        trie = self.trie
        res = 0
        for d1, d2 in zip(digits, tgt):
            t = d1 ^ d2
            if d2 == 1:
                if t not in trie:
                    break
                _, trie = trie[t]
            else:
                res += trie.get(1-t, [0, {}])[0]
                _, trie = trie.get(t, [0, {}])
        res += trie.get("eos", 0)
        return res
        
    def find(self, digits, low, high):
        trie = self.trie
        l = self.find_low(digits, high)
        h = self.find_high(digits, low)
        tot = self.trie.get(0, [0, {}])[0] + self.trie.get(1, [0, {}])[0]
        return max(l+h-tot, 0)
        
# === 4812ms && 28.5MB === #
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def num2digit(n):
            digits = []
            for i in range(16):
                digits.insert(0, n % 2)
                n = n // 2
            return digits
        
        low = num2digit(low)
        high = num2digit(high)
        trie = Trie()
        res = 0
        for x in nums:
            x = num2digit(x)
            res += trie.find(x, low, high)
            trie.add(x)
        return res
                
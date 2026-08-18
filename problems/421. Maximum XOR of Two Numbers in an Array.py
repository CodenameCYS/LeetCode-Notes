'''
=== 421. Maximum XOR of Two Numbers in an Array ===

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
    Input: [3, 10, 5, 25, 2, 8]
    Output: 28
    Explanation: The maximum result is 5 ^ 25 = 28.
'''
class Trie:
    def __init__(self, nums):
        self.trie = {}
        for num in nums:
            self.add(num)
            
    def num2digit(self, num):
        digit = []
        for _ in range(31):
            digit.insert(0, num % 2)
            num = num // 2
        return digit
    
    def add(self, num):
        digit = self.num2digit(num)
        trie = self.trie
        for d in digit:
            trie = trie.setdefault(d, {})
        trie["eos"] = num
        
    def find_complementary(self, num):
        digit = self.num2digit(num)
        trie = self.trie
        for d in digit:
            trie = trie[1-d] if 1-d in trie else trie[d]
        return trie["eos"]

# === 588ms(45.27%) && 99.1MB(44.90%) === #
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        trie = Trie(nums)
        for x in nums:
            y = trie.find_complementary(x)
            # print(x, y)
            ans = max(ans, x^y)
        return ans
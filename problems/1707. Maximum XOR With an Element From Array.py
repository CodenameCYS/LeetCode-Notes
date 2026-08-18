'''
=== 1707. Maximum XOR With an Element From Array ===

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

Example 1:
    Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
    Output: [3,3,7]
    Explanation:
    1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
    2) 1 XOR 2 = 3.
    3) 5 XOR 2 = 7.
Example 2:
    Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
    Output: [15,-1,5]
 
Constraints:
    1. 1 <= nums.length, queries.length <= 105
    2. queries[i].length == 2
    3. 0 <= nums[j], xi, mi <= 109
'''
# === 6567ms && 256.1MB === #
class Trie:
    def __init__(self):
        self.trie = {}
        
    def num2digits(self, n):
        digits = [0 for _ in range(30)]
        idx = 29
        while n != 0:
            digits[idx] = n % 2
            n = n // 2
            idx -= 1
        return digits
    
    def add(self, n):
        digits = self.num2digits(n)
        
        trie = self.trie
        for d in digits:
            trie = trie.setdefault(d, {})
        trie["eos"] = n
        return
    
    def find(self, x, m):
        digits = self.num2digits(x)
        
        stack = [(self.trie, 0, 0)]
        while stack:
            trie, val, depth = stack.pop()
            if depth == 30:
                return x ^ trie["eos"]
            new_val = val + 2**(29-depth)
            if digits[depth] == 0:
                if 0 in trie:
                    stack.append((trie[0], val, depth+1))
                if 1 in trie and new_val <= m:
                    stack.append((trie[1], new_val, depth+1))
            else:
                if 1 in trie and new_val <= m:
                    stack.append((trie[1], new_val, depth+1))
                if 0 in trie:
                    stack.append((trie[0], val, depth+1))
        return -1

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        for n in nums:
            trie.add(n)
            
        res = [trie.find(x, m) for x, m in queries]
        return res
            
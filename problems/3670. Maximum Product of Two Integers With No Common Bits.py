'''
=== 3670. Maximum Product of Two Integers With No Common Bits ===

You are given an integer array nums.
Your task is to find two distinct indices i and j such that the product nums[i] * nums[j] is maximized, and the binary representations of nums[i] and nums[j] do not share any common set bits.
Return the maximum possible product of such a pair. If no such pair exists, return 0.

Example 1:
    Input: nums = [1,2,3,4,5,6,7]
    Output: 12
    Explanation:
    The best pair is 3 (011) and 4 (100). They share no set bits and 3 * 4 = 12.
Example 2:
    Input: nums = [5,6,4]
    Output: 0
    Explanation:
    Every pair of numbers has at least one common set bit. Hence, the answer is 0.
Example 3:
    Input: nums = [64,8,32]
    Output: 2048
    Explanation:
    No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 (64 * 32 = 2048).

Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] <= 106
'''
DIGIT_NUM = 20

class Trie:
    def __init__(self):
        self.trie = {}
    
    def add(self, num):
        word = bin(num)[2:].rjust(DIGIT_NUM, "0")
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = num

    @lru_cache(None)
    def find(self, num):
        word = bin(num)[2:].rjust(DIGIT_NUM, "0")
        trie = self.trie

        def dfs(idx, trie):
            if idx == DIGIT_NUM:
                return trie.get("eos", 0)
            if trie == {}:
                return 0
            if word[idx] == "1":
                return dfs(idx+1, trie["0"]) if "0" in trie else 0
            else:
                return max(dfs(idx+1, trie.get("0", {})), dfs(idx+1, trie.get("1", {})))
        
        return dfs(0, trie)

@lru_cache(None)
def get_rev(num):
    num = bin(num)[2:]
    digits = [1-int(x) for x in num]
    ans = 0
    for d in digits:
        ans = 2*ans+d
    return ans
# === 16912ms && 319.43MB === #
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        snums = set(nums)
        nums = list(snums)
        trie = Trie()
        for num in nums:
            # print(bin(num)[2:].rjust(DIGIT_NUM, "0"))
            trie.add(num)

        nums = sorted(nums, reverse=True)
        ans = 0
        for num in nums:
            rev = get_rev(num)
            if num * num <= ans:
                break
            if get_rev(num) in snums:
                ans = max(ans, num * get_rev(num))
                continue
            ans = max(ans, num * trie.find(num))
        return ans
        
        # return max([num*trie.find(num) for num in nums])
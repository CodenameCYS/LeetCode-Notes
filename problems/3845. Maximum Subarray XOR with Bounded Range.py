'''
=== 3845. Maximum Subarray XOR with Bounded Range ===

You are given a non-negative integer array nums and an integer k.
You must select a subarray of nums such that the difference between its maximum and minimum elements is at most k. The value of this subarray is the bitwise XOR of all elements in the subarray.
Return an integer denoting the maximum possible value of the selected subarray.

Example 1:
    Input: nums = [5,4,5,6], k = 2
    Output: 7
    Explanation:
    Select the subarray [5, 4, 5, 6].
    The difference between its maximum and minimum elements is 6 - 4 = 2 <= k.
    The value is 4 XOR 5 XOR 6 = 7.
Example 2:
    Input: nums = [5,4,5,6], k = 1
    Output: 6
    Explanation:
    Select the subarray [5, 4, 5, 6].
    The difference between its maximum and minimum elements is 6 - 6 = 0 <= k.
    The value is 6.
 
Constraints:
    1. 1 <= nums.length <= 4 * 104
    2. 0 <= nums[i] < 215
    3. 0 <= k < 215
'''
# === 3864ms && 38.95MB === #
def num2bin(num):
    ans = bin(num)[2:].rjust(15, "0")
    return ans

class Trie:
    def __init__(self):
        self.trie = {}  
        self.cnt = defaultdict(int)
    
    def add(self, num):
        word = num2bin(num)
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = num
        self.cnt[num] += 1

    def delete(self, num):
        self.cnt[num] -= 1
        if self.cnt[num] == 0:
            word = num2bin(num)
            n = len(word)
            def _delete(idx, trie):
                if idx >= n:
                    trie.pop("eos")
                    return
                _delete(idx+1, trie[word[idx]])
                if trie[word[idx]] == {}:
                    trie.pop(word[idx])
                return
            _delete(0, self.trie)
        return

    def find(self, num):
        word = num2bin(num)
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "eos" in trie

    def query(self, num):
        word = num2bin(num)
        trie = self.trie
        for c in word:
            rc = "1" if c == "0" else "0"
            if rc in trie:
                trie = trie[rc]
            else:
                trie = trie[c]
        return trie["eos"]


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        n = len(nums)
        window = []
        trie = Trie()
        prefi, prefj = 0, 0
        i, j = 0, 0
        ans = 0
        while i < n:
            while j < n and (window == [] or (abs(nums[j] - window[0]) <= k and abs(nums[j] - window[-1]) <= k)):
                bisect.insort(window, nums[j])
                prefj = prefj ^ nums[j]
                trie.add(prefj)
                j += 1
            ans = max(ans, trie.query(prefi) ^ prefi)
            prefi = prefi ^ nums[i]
            trie.delete(prefi)
            window.pop(bisect.bisect_left(window, nums[i]))
            i += 1
        return ans
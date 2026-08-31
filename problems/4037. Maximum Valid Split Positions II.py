'''
=== 4037. Maximum Valid Split Positions II ===

You are given an integer array nums.
You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.
A split position i of arr is valid if:
    - 0 <= i < m - 1, and
    - gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
An array of length 1 has no valid split positions.
The score of arr is the number of valid split positions in it.
Return the maximum possible score of arr.
Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

Example 1:
    Input: nums = [10,30,15,10]
    Output: 2
    Explanation:
    One optimal solution is to remove nums[2] = 15. Then arr = [10, 30, 10].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	10	10
    1	10	10
    All split positions are valid. Thus, the answer is 2.
Example 2:
    Input: nums = [2,10,14]
    Output: 1
    Explanation:
    One optimal solution is to not remove any element. Then arr = [2, 10, 14].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	2	2
    1	2	14
    Only the split position at index 0 is valid. Thus, the answer is 1.
Example 3:
    Input: nums = [2,4]
    Output: 0
    Explanation:
    The only remaining array that has a split position is arr = [2, 4].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	2	4
    There are no valid split positions. Thus, the answer is 0.

Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] <= 109​​​​​​​
'''
# === 904ms && 33.11MB === #
class Solution:
    def countValidSplit(self, nums: list[int], skip: int) -> int:
        n = len(nums)
        # suf[i] 是后缀 [i,n-1]（除去 skip）的 GCD
        suf = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            if j != skip:
                suf[j] = gcd(suf[j + 1], nums[j])
            else:
                suf[j] = suf[j + 1]

        cnt = pre = 0
        for j, x in enumerate(nums):
            if j != skip:
                pre = gcd(pre, x)
                # 现在 pre 是前缀 [0,j]（除去 skip）的 GCD
                if pre == suf[j + 1]:
                    cnt += 1
        return cnt

    def maxValidSplits(self, nums: list[int]) -> int:
        ans = self.countValidSplit(nums, -1)  # 不删除元素

        # countValidSplit 只会调用 O(log max(nums)) 次
        g = 0
        for i, x in enumerate(nums):
            if g > 0 and x % g == 0:  # x 不改变前缀 GCD
                continue
            g = gcd(g, x)
            ans = max(ans, self.countValidSplit(nums, i))

        return ans

'''
=== 923. 3Sum With Multiplicity ===

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
As the answer can be very large, return it modulo 109 + 7.

Example 1:
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: 
    Enumerating by the values (arr[i], arr[j], arr[k]):
    (1, 2, 5) occurs 8 times;
    (1, 3, 4) occurs 8 times;
    (2, 2, 4) occurs 2 times;
    (2, 3, 3) occurs 2 times.
Example 2:
    Input: arr = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation: 
    arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
    We choose one 1 from [1,1] in 2 ways,
    and two 2s from [2,2,2,2] in 6 ways.
 
Constraints:
    1. 3 <= arr.length <= 3000
    2. 0 <= arr[i] <= 100
    3. 0 <= target <= 300
'''
# === 72ms(92.48%) && 14.4MB(53.76%) === #
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(arr)
        elems = sorted(cnt.keys())
        # print(cnt)
        # print(elems)
        n = len(elems)
        res = 0
        for i, x in enumerate(elems):
            # print(i, x, res)
            if 3*x == target:
                if cnt[x] >= 3:
                    res += cnt[x]*(cnt[x]-1)*(cnt[x]-2) // 6
            elif target - 2*x in cnt:
                res += cnt[target - 2*x] * cnt[x]*(cnt[x]-1) // 2
            for j in range(i+1, n):
                if target - x - elems[j] <= elems[j]:
                    break
                res +=  cnt[x] * cnt[elems[j]] * cnt.get(target-x-elems[j], 0)
        # print("=" * 10)
        return res % MOD
                    
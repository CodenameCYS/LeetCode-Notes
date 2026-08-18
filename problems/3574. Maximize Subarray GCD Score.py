'''
=== 3574. Maximize Subarray GCD Score ===

You are given an array of positive integers nums and an integer k.
You may perform at most k operations. In each operation, you can choose one element in the array and double its value. Each element can be doubled at most once.
The score of a contiguous subarray is defined as the product of its length and the greatest common divisor (GCD) of all its elements.
Your task is to return the maximum score that can be achieved by selecting a contiguous subarray from the modified array.
Note:
The greatest common divisor (GCD) of an array is the largest integer that evenly divides all the array elements.
 
Example 1:
    Input: nums = [2,4], k = 1
    Output: 8
    Explanation:
    Double nums[0] to 4 using one operation. The modified array becomes [4, 4].
    The GCD of the subarray [4, 4] is 4, and the length is 2.
    Thus, the maximum possible score is 2 × 4 = 8.
Example 2:
    Input: nums = [3,5,7], k = 2
    Output: 14
    Explanation:
    Double nums[2] to 14 using one operation. The modified array becomes [3, 5, 14].
    The GCD of the subarray [14] is 14, and the length is 1.
    Thus, the maximum possible score is 1 × 14 = 14.
Example 3:
    Input: nums = [5,5,5], k = 1
    Output: 15
    Explanation:
    The subarray [5, 5, 5] has a GCD of 5, and its length is 3.
    Since doubling any element doesn't improve the score, the maximum score is 3 × 5 = 15.
 
Constraints:
    1. 1 <= n == nums.length <= 1500
    2. 1 <= nums[i] <= 109
    3. 1 <= k <= n
'''
def get_primes(n):
    primes = set()
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**5)
# === 13858ms && 19.2MB === #
class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len(set(nums)) == 1:
            return max(n * nums[0], min(n, k) * 2 * nums[0])

        divisors = set()
        for i in range(n):
            _gcd = 2*nums[i]
            divisors.add(nums[i])
            divisors.add(_gcd)
            if _gcd in divisors and _gcd in PRIMES:
                continue
            for j in range(i+1, n):
                _gcd = gcd(_gcd, 2*nums[j])
                divisors.add(_gcd)
                if _gcd == 1 or _gcd in PRIMES:
                    break

        ans = 0
        divisors = sorted(divisors, reverse=True)
        for div in divisors:
            if div * n <= ans:
                break
            op, cnt = 0, 0
            for i, num in enumerate(nums):
                if div * (n-i+cnt) <= ans:
                    break
                if num % div == 0:
                    pass
                elif (num * 2) % div == 0:
                    op += 1
                else:
                    op, cnt = 0, 0
                    continue
                cnt += 1
                while cnt > 0 and op > k:
                    li = i - cnt + 1
                    if nums[li] % div != 0:
                        op -= 1
                    cnt -= 1
                ans = max(ans, cnt * div)
        return ans
                    
                


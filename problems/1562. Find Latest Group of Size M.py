'''
=== 1562. Find Latest Group of Size M ===

Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.
At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.
Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

Example 1:
    Input: arr = [3,5,1,2,4], m = 1
    Output: 4
    Explanation:
    Step 1: "00100", groups: ["1"]
    Step 2: "00101", groups: ["1", "1"]
    Step 3: "10101", groups: ["1", "1", "1"]
    Step 4: "11101", groups: ["111", "1"]
    Step 5: "11111", groups: ["11111"]
    The latest step at which there exists a group of size 1 is step 4.
Example 2:
    Input: arr = [3,1,5,4,2], m = 2
    Output: -1
    Explanation:
    Step 1: "00100", groups: ["1"]
    Step 2: "10100", groups: ["1", "1"]
    Step 3: "10101", groups: ["1", "1", "1"]
    Step 4: "10111", groups: ["1", "111"]
    Step 5: "11111", groups: ["11111"]
    No group of size 2 exists during any step.
Example 3:
    Input: arr = [1], m = 1
    Output: 1
Example 4:
    Input: arr = [2,1], m = 2
    Output: 2
 
Constraints:
    1. n == arr.length
    2. 1 <= n <= 10^5
    3. 1 <= arr[i] <= n
    4. All integers in arr are distinct.
    5. 1 <= m <= arr.length
'''
# === 1696ms && 27.8MB === #
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        start_set = {}
        end_set = {}
        counter = 0
        for idx, n in enumerate(arr):
            if n - 1 in end_set and n + 1 in start_set:
                st = end_set.pop(n-1)
                ed = start_set.pop(n+1)
                end_set[ed] = st
                start_set[st] = ed
                if n - st == m:
                    counter -= 1
                if ed - n == m:
                    counter -= 1
                if ed - st + 1 == m:
                    counter += 1
            elif n - 1 in end_set:
                st = end_set.pop(n-1)
                end_set[n] = st
                start_set[st] = n
                if n - st == m:
                    counter -= 1
                elif n-st+1 == m:
                    counter += 1
            elif n + 1 in start_set:
                ed = start_set.pop(n+1)
                start_set[n] = ed
                end_set[ed] = n
                if ed - n == m:
                    counter -= 1
                elif ed-n+1 == m:
                    counter += 1
            else:
                start_set[n] = n
                end_set[n] = n
                if m == 1:
                    counter += 1
            if counter > 0:
                ans = idx + 1
        return ans
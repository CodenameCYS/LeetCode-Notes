'''
=== 2269. Find the K-Beauty of a Number ===

The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
    - It has a length of k.
    - It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:
    - Leading zeros are allowed.
    - 0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example 1:
    Input: num = 240, k = 2
    Output: 2
    Explanation: The following are the substrings of num of length k:
    - "24" from "240": 24 is a divisor of 240.
    - "40" from "240": 40 is a divisor of 240.
    Therefore, the k-beauty is 2.
Example 2:
    Input: num = 430043, k = 2
    Output: 2
    Explanation: The following are the substrings of num of length k:
    - "43" from "430043": 43 is a divisor of 430043.
    - "30" from "430043": 30 is not a divisor of 430043.
    - "00" from "430043": 0 is not a divisor of 430043.
    - "04" from "430043": 4 is not a divisor of 430043.
    - "43" from "430043": 43 is a divisor of 430043.
    Therefore, the k-beauty is 2.
 
Constraints:
    1. 1 <= num <= 109
    2. 1 <= k <= num.length (taking num as a string)
'''
# === 29ms && 13.8MB === #
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        res = 0
        for i in range(n-k+1):
            sub = int(s[i:i+k])
            if sub == 0:
                continue
            if num % sub == 0:
                # print(sub)
                res += 1
        return res
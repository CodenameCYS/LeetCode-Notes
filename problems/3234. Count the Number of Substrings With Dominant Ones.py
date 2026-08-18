'''
=== 3234. Count the Number of Substrings With Dominant Ones ===

You are given a binary string s.
Return the number of substrings with dominant ones.
A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

Example 1:
    Input: s = "00011"
    Output: 5
    Explanation:
    The substrings with dominant ones are shown in the table below.
        i	j	s[i..j]	Number of Zeros	Number of Ones
        3	3	1	0	1
        4	4	1	0	1
        2	3	01	1	1
        3	4	11	0	2
        2	4	011	1	2
Example 2:
    Input: s = "101101"
    Output: 16
    Explanation:
    The substrings with non-dominant ones are shown in the table below.
    Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
        i	j	s[i..j]	Number of Zeros	Number of Ones
        1	1	0	1	0
        4	4	0	1	0
        1	4	0110	2	2
        0	4	10110	2	3
        1	5	01101	2	3
 
Constraints:
    1. 1 <= s.length <= 4 * 104
    2. s consists only of characters '0' and '1'.
'''
# === 7478ms && 18.4MB === #
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == "0"]
        if len(zeros) <= 1:
            return n * (n+1) // 2 - len(zeros)
        
        m = len(zeros)
        ans = (n-1 - zeros[-1]) * (n - zeros[-1]) // 2
        for i in range(m):
            if i == 0:
                one = zeros[i]
            else:
                one = zeros[i] - zeros[i-1]-1
            ans += one*(one+1) // 2
        # print(ans)
        for i in range(1, m+1):
            if i*i+i > n:
                break
            for j in range(m+1-i):
                l, r = zeros[j], zeros[i+j-1]
                mid = r-l+1-i
                l1 = l if j == 0 else zeros[j] - zeros[j-1]-1
                r1 = n-1-r if i+j-1 == m-1 else zeros[i+j] - zeros[i+j-1]-1
                if mid >= i*i:
                    need = 0
                    cnt = (l1+1) * (r1+1)
                elif mid + l1 + r1 >= i*i:
                    need = i*i-mid
                    cnt = (l1+r1-need+1) * (l1+r1-need+2) // 2
                    if l1 >= need:
                        cnt = cnt - ((l1-need+1) * (l1-need+2) // 2) + (l1-need+1)
                    if r1 >= need:
                        cnt = cnt - ((r1-need+1) * (r1-need+2) // 2) + (r1-need+1)
                else:
                    need = 0
                    cnt = 0
                ans += cnt
        return ans
                
'''
=== 6. Zigzag Conversion ===

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
    
Constraints:
    1. 1 <= s.length <= 1000
    2. s consists of English letters (lower-case and upper-case), ',' and '.'.
    3. 1 <= numRows <= 1000
'''
# === 9ms && 19.35MB === #
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        subs = [[] for _ in range(numRows)]
        idx, row = 0, 0
        while idx < n:
            while idx < n and row < numRows-1:
                subs[row].append(s[idx])
                idx += 1
                row += 1
            while idx < n and row > 0:
                subs[row].append(s[idx])
                idx += 1
                row -= 1
        return "".join(["".join(sub) for sub in subs])
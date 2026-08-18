'''
=== 2075. Decode the Slanted Ciphertext ===

A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.
originalText is placed first in a top-left to bottom-right manner.
The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.
encodedText is then formed by appending all characters of the matrix in a row-wise fashion.
The characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.
For example, if originalText = "cipher" and rows = 3, then we encode it in the following manner:
The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = "ch ie pr".
Given the encoded string encodedText and number of rows rows, return the original string originalText.
Note: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one possible originalText.

Example 1:
    Input: encodedText = "ch   ie   pr", rows = 3
    Output: "cipher"
    Explanation: This is the same example described in the problem description.
Example 2:
    Input: encodedText = "iveo    eed   l te   olc", rows = 4
    Output: "i love leetcode"
    Explanation: The figure above denotes the matrix that was used to encode originalText. 
    The blue arrows show how we can find originalText from encodedText.
Example 3:
    Input: encodedText = "coding", rows = 1
    Output: "coding"
    Explanation: Since there is only 1 row, both originalText and encodedText are the same.
Example 4:
    Input: encodedText = " b  ac", rows = 2
    Output: " abc"
    Explanation: originalText cannot have trailing spaces, but it may be preceded by one or more spaces.
 
Constraints:
    1. 0 <= encodedText.length <= 106
    2. encodedText consists of lowercase English letters and ' ' only.
    3. encodedText is a valid encoding of some originalText that does not have trailing spaces.
    4. 1 <= rows <= 1000
    5. The testcases are generated such that there is only one possible originalText.
'''
# === 684ms && 27.1MB === #
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        m = n // rows
        rows = min(m, rows)
        s = []
        for i in range(rows):
            s.append(encodedText[i*m:(i+1)*m][i:])
        
        if s == []:
            return ""
        
        res = ""
        for j in range(len(s[0])):
            for i in range(rows):
                if j < len(s[i]):
                    res += s[i][j]
        return res.rstrip()
        
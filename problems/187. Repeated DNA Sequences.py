'''
=== 187. Repeated DNA Sequences ===

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
 
Constraints:
    1. 0 <= s.length <= 105
    2. s[i] is 'A', 'C', 'G', or 'T'.
'''
# === 72ms(48.18%) && 27.7MB === #
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        n = len(s)
        if n < 10:
            return []
        for i in range(n-9):
            counter[s[i:i+10]] += 1
        return [x for x in counter if counter[x] > 1]
        
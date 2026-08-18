'''
=== 17. Letter Combinations of a Phone Number ===

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
    - Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
# === 48ms(5.52%) && 12.6MB(100%) === #
class Solution:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mapping = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl",
                        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        if len(digits) == 1:
            return list(self.mapping[digits])
        tmp = self.letterCombinations(digits[1:])
        ans = []
        for c in self.mapping[digits[0]]:
            ans.extend([c + it for it in tmp])
        return ans
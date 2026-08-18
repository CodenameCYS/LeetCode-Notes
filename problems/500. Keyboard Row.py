'''
# === 500. Keyboard Row === #

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]
 
Note:
    1. You may use one character in the keyboard more than once.
    2. You may assume the input string will only contain letters of alphabet.
'''
# === 24ms(86.73%) && 12.7MB(100%) === #
class Solution:
    def __init__(self):
        self.alphabet = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if word == "":
                ans.append(word)
            s = word.lower()
            for i in range(3):
                if s[0] in self.alphabet[i]:
                    charset = self.alphabet[i]
                    break
            need_add = True
            for c in s:
                if c not in charset:
                    need_add = False
                    break
            if need_add:
                ans.append(word) 
        return ans
            
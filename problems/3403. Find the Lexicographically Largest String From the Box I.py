'''
=== 3403. Find the Lexicographically Largest String From the Box I ===

You are given a string word, and an integer numFriends.
Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
    - word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
    - All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.
A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.

Example 1:
    Input: word = "dbca", numFriends = 2
    Output: "dbc"
    Explanation: 
    All possible splits are:
    "d" and "bca".
    "db" and "ca".
    "dbc" and "a".
Example 2:
    Input: word = "gggg", numFriends = 4
    Output: "g"
    Explanation: 
    The only possible split is: "g", "g", "g", and "g".

Constraints:
    1. 1 <= word.length <= 5 * 103
    2. word consists only of lowercase English letters.
    3. 1 <= numFriends <= word.length
'''
# === 4ms && 18MB === #
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_char = max(word)
        ans = max_char
        for i, ch in enumerate(word):
            if ch != max_char:
                continue
            if i >= numFriends-1:
                tmp = word[i:]
            else:
                need = numFriends - i
                tmp = word[i:n-(numFriends - 1 - i)]
            ans = max(ans, tmp)
        return ans
            
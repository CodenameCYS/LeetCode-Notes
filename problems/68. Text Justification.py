'''
=== 68. Text Justification ===

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
    - A word is defined as a character sequence consisting of non-space characters only.
    - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    - The input array words contains at least one word.
 
Example 1:
    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
Example 2:
    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified becase it contains only one word.
Example 3:
    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
    [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
 
Constraints:
    1. 1 <= words.length <= 300
    2. 1 <= words[i].length <= 20
    3. words[i] consists of only English letters and symbols.
    4. 1 <= maxWidth <= 100
    5. words[i].length <= maxWidth
'''
# === 47ms(12.60%) && 14.2MB(78.31%) === #
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, cnt = [], 0
        for w in words:
            if cnt + len(w) > maxWidth:
                res.append(line)
                cnt = 0
                line = []
            line.append(w)
            cnt += len(w)+1
        if line != []:
            res.append(line)

        def padding(line, maxWidth):
            if len(line) == 1:
                return line[0] + " " * (maxWidth - len(line[0]))
            blank, gap = maxWidth - sum(len(w) for w in line), len(line) - 1
            base, delta = blank // gap, blank % gap
            # print(blank, gap, base, delta)
            res = ""
            for i, w in enumerate(line[:-1]):
                res += w + base*" "
                if i < delta:
                    res += " "
            return res + line[-1]

        res = [padding(line, maxWidth) for line in res[:-1]] + [" ".join(res[-1]).ljust(maxWidth)]
        return res
            

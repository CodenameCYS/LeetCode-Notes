'''
=== 1736. Latest Time by Replacing Hidden Digits ===

You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
    Input: time = "2?:?0"
    Output: "23:50"
    Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:
    Input: time = "0?:3?"
    Output: "09:39"
Example 3:
    Input: time = "1?:22"
    Output: "19:22"
 
Constraints:
    1. time is in the format hh:mm.
    2. It is guaranteed that you can produce a valid time from the given string.
'''
# === 20ms && 14.1MB === #
class Solution:
    def maximumTime(self, time: str) -> str:
        s = list(time)
        for idx, c in enumerate(s):
            if c != '?':
                continue
            if idx == 0:
                if time[idx+1] in "0123?":
                    s[idx] = '2'
                else:
                    s[idx] = "1"
            elif idx == 1:
                if s[idx-1] == "2":
                    s[idx] = "3"
                else:
                    s[idx] = "9"
            elif idx == 3:
                s[idx] = "5"
            else:
                s[idx] = '9'
        return "".join(s)
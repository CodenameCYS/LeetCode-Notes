'''
=== 3114. Latest Time You Can Obtain After Replacing Characters ===

You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".
12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.
You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.
Return the resulting string.

Example 1:
    Input: s = "1?:?4"
    Output: "11:54"
    Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".
Example 2:
    Input: s = "0?:5?"
    Output: "09:59"
    Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

Constraints:
    1. s.length == 5
    2. s[2] is equal to the character ":".
    3. All characters except s[2] are digits or "?" characters.
    4. The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.
'''
# === 30ms && 16.4MB === #
class Solution:
    def findLatestTime(self, s: str) -> str:
        hour, minute = s.split(":")
        
        def get_max(s, _max):
            if "?" not in s:
                return s
            elif s == "??":
                return str(_max)
            elif s[0] == "?":
                for ch in "9876543210":
                    if int(ch + s[1]) <= _max:
                        return ch + s[1]
            else:
                for ch in "9876543210":
                    if int(s[0] + ch) <= _max:
                        return s[0] + ch
                    
        return get_max(hour, 11) + ":" + get_max(minute, 59)
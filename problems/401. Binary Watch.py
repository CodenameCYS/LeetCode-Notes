'''
=== 401. Binary Watch ===

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:
    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
    1. The order of output does not matter.
    2. The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    3. The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''
# === 24ms(94.72%) && 12.8MB(100%) === #
class Solution:
    def possible_time(self, h, m):
        if h < 0 or h >= 4 or m < 0 or m >= 6:
            return []
        ans = []
        for hour in itertools.combinations([1,2,4,8], h):
            hour = sum(hour)
            if hour >= 12:
                continue
            for miniute in itertools.combinations([1,2,4,8,16,32], m):
                miniute = sum(miniute)
                if miniute >= 60:
                    continue
                ans.append("%d:%02d" % (hour, miniute))
        return ans
    
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for i in range(num+1):
            ans.extend(self.possible_time(i, num-i))
        return ans
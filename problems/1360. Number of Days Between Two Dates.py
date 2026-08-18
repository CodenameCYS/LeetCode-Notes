'''
=== 1360. Number of Days Between Two Dates ===

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1
Example 2:
    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15
 
Constraints:
    1. The given dates are valid dates between the years 1971 and 2100.
'''
# === 24ms && 12.7MB === #
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        d1 = [int(it) for it in date1.split("-")]
        d1 = datetime(d1[0], d1[1], d1[2])
        d2 = [int(it) for it in date2.split("-")]
        d2 = datetime(d2[0], d2[1], d2[2])
        return abs((d2-d1).days)
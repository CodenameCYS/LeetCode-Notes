'''
=== 2259. Remove Digit From Number to Maximize Result ===

You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

Example 1:
    Input: number = "123", digit = "3"
    Output: "12"
    Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:
    Input: number = "1231", digit = "1"
    Output: "231"
    Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
    Since 231 > 123, we return "231".
Example 3:
    Input: number = "551", digit = "5"
    Output: "51"
    Explanation: We can remove either the first or second '5' from "551".
    Both result in the string "51".
 
Constraints:
    1. 2 <= number.length <= 100
    2. number consists of digits from '1' to '9'.
    3. digit is a digit from '1' to '9'.
    4. digit occurs at least once in number.
'''
# === 77ms && 13.9MB === #
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = -1
        n = len(number)
        for i in range(n-1):
            if number[i] == digit:
                if number[i] < number[i+1]:
                    return number[:i] + number[i+1:]
                last = i
        if number[-1] == digit:
            last = n-1
        return number[:last] + number[last+1:]
                
                
        
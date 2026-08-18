'''
=== 3606. Coupon Code Validator ===

You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
    - code[i]: a string representing the coupon identifier.
    - businessLine[i]: a string denoting the business category of the coupon.
    - isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:
    - code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
    - businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
    - isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

Example 1:
    Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
    Output: ["PHARMA5","SAVE20"]
    Explanation:
    First coupon is valid.
    Second coupon has empty code (invalid).
    Third coupon is valid.
    Fourth coupon has special character @ (invalid).
Example 2:
    Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]
    Output: ["ELECTRONICS_50"]
    Explanation:
    First coupon is inactive (invalid).
    Second coupon is valid.
    Third coupon has invalid business line (invalid).

Constraints:
    1. n == code.length == businessLine.length == isActive.length
    2. 1 <= n <= 100
    3. 0 <= code[i].length, businessLine[i].length <= 100
    4. code[i] and businessLine[i] consist of printable ASCII characters.
    5. isActive[i] is either true or false.
'''
# === 11ms && 17.81MB === #
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ValidChars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_"

        def is_valid(_code, business_line, is_active):
            if is_active is not True:
                return False
            if business_line not in {"electronics", "grocery", "pharmacy", "restaurant"}:
                return False
            if _code == "" or any(ch not in ValidChars for ch in _code):
                return False
            return True

        ans = []
        for _code, business_line, is_active in zip(code, businessLine, isActive):
            if is_valid(_code, business_line, is_active):
                ans.append((_code, business_line, is_active))
        ans = sorted(ans, key=lambda x: (x[1], x[0]))
        ans = [x[0] for x in ans]
        return ans
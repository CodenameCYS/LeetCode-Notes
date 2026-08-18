'''
=== 65. Valid Number ===

Validate if a given string can be interpreted as a decimal number.
    Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    " -90e3   " => true
    " 1e" => false
    "e3" => false
    " 6e-1" => true
    " 99e2.5 " => false
    "53.5e93" => true
    " --6 " => false
    "-+3" => false
    "95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
    1. Numbers 0-9
    2. Exponent - "e"
    3. Positive/negative sign - "+"/"-"
    4. Decimal point - "."
    5. Of course, the context of these characters also matters in the input.

Update (2015-02-10):
    - The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''
# === 28ms(88.03%) && 12.&MB(100%) === #
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            n = float(s)
            return True
        except:
            return False
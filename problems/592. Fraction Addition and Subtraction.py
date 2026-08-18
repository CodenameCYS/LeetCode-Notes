'''
=== 592. Fraction Addition and Subtraction ===

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
    Input:"-1/2+1/2"
    Output: "0/1"
Example 2:
    Input:"-1/2+1/2+1/3"
    Output: "1/3"
Example 3:
    Input:"1/3-1/2"
    Output: "-1/6"
Example 4:
    Input:"5/3+1/3"
    Output: "2/1"

Note:
    1. The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    2. Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    3. The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    4. The number of given fractions will be in the range [1,10].
    5. The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''
# === 28ms(78.99%) && 12.6MB(100%) === #
class Solution:
    def gcd(self, a, b):
        a = abs(a); b = abs(b)
        a, b = (a, b) if a >=b else (b, a)
        while b:
            a,b = b,a%b
        return a
    
    def add(self, s1, s2):
        a1, b1 = [int(it) for it in s1.split("/")]
        a2, b2 = [int(it) for it in s2.split("/")]
        a = a1*b2 + a2*b1
        b = b1*b2
        if a == 0:
            return "0/1"
        k = self.gcd(a,b)
        return "{}/{}".format(a//k, b//k)
    
    def fractionAddition(self, expression: str) -> str:
        nums = expression.replace("-", "+-").strip("+").split("+")
        ans = "0/1"
        for n in nums:
            ans = self.add(ans, n)
        return ans
        
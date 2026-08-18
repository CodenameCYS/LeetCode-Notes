'''
=== 224. Basic Calculator ===

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
    Input: s = "1 + 1"
    Output: 2
Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3
Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23
 
Constraints:
    1. 1 <= s.length <= 3 * 105
    2. s consists of digits, '+', '-', '(', ')', and ' '.
    3. s represents a valid expression.
    4. '+' is not used as a unary operation.
    5. '-' could be used as a unary operation but it has to be inside parentheses.
    6. There will be no two consecutive operators in the input.
    7. Every number and running calculation will fit in a signed 32-bit integer.
'''
# === 152ms && 15.7MB === #
class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        
        def _cal_plus_and_minus(nums, ops):
            i, n = 0, len(ops)
            for i in range(n):
                x = nums[i]
                y = nums[i+1]
                op = ops[i]
                num = x + y if op == "+" else x - y
                nums[i+1] = num
            return nums[-1]

        def _cal_mul_and_div(nums, ops):
            if ops != [] and ops[-1] in "*/":
                y = nums.pop()
                x = nums.pop()
                num = x * y if ops[-1] == "*" else x / y
                nums.append(num)  
            return
        
        stack = []
        nums, ops = [], []
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "(":
                stack.append([nums, ops])
                nums, ops = [], []
                i += 1
            elif s[i] == ")":
                num = _cal_plus_and_minus(nums, ops)
                nums, ops = stack.pop()
                nums.append(num)
                _cal_mul_and_div(nums, ops)
                i += 1
            elif s[i] in "+-*/":
                ops.append(s[i])
                if nums == []:
                    nums.append(0)
                i += 1
            else:
                num = 0
                while i < n and s[i] in "0123456789":
                    num = 10 * num + int(s[i])
                    i += 1   
                nums.append(num)
                _cal_mul_and_div(nums, ops)
    
        return _cal_plus_and_minus(nums, ops)
            
        
                
        
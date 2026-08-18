'''
=== 640. Solve the Equation ===

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.
    1. If there is no solution for the equation, return "No solution".
    2. If there are infinite solutions for the equation, return "Infinite solutions".
    3. If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
    Input: "x+5-3+x=6+x-2"
    Output: "x=2"
Example 2:
    Input: "x=x"
    Output: "Infinite solutions"
Example 3:
    Input: "2x=x"
    Output: "x=0"
Example 4:
    Input: "2x+3x-6x=x+2"
    Output: "x=-1"
Example 5:
    Input: "x=x+2"
    Output: "No solution"
'''
# === 16ms(100%) && 12.8MB(100%) === #
class Solution:
    def x2num(self, expression):
        if expression == "x":
            return 1
        elif expression == "-x":
            return -1
        else:
            return int(expression[:-1])
        
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split("=")
        l = l.replace("-", "+-").strip("+").split("+")
        lx = sum([self.x2num(it) for it in l if it[-1] == "x"])
        lnum = sum([int(it) for it in l if it[-1] != "x"])
        r = r.replace("-", "+-").strip("+").split("+")
        rx = sum([self.x2num(it) for it in r if it[-1] == "x"])
        rnum = sum([int(it) for it in r if it[-1] != "x"])
        if lx == rx:
            return "No solution" if lnum != rnum else "Infinite solutions"
        else:
            return "x={}".format((rnum-lnum) // (lx-rx))
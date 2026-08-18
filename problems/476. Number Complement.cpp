/*
=== 476. Number Complement ===

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
- The given integer is guaranteed to fit within the range of a 32-bit signed integer.
- You could assume no leading zero bit in the integer’s binary representation.

Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
*/
// === 0ms(100%) && 6.9MB(100%) === //
int findComplement(int num){
    long ans = 0;
    long flag = 1;
    while(num != 0){
        ans += (1-num%2)*flag;
        num /= 2;
        flag *= 2;
    }
    return ans;
}


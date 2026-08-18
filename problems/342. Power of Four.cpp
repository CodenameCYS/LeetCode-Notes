/*
=== 342. Power of Four ===

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
    Input: 16
    Output: true
Example 2:
    Input: 5
    Output: false

- Follow up: Could you solve it without loops/recursion?
*/
// === 4ms(100%) & 7MB(6.67%) === //
bool isPowerOfFour(int num) {
    double temp = log(num)/log(4);
    return temp == (int)temp;
}
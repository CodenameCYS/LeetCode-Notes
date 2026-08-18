/*
=== 633. Sum of Square Numbers ===

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
    Input: 3
    Output: False
*/
// === 4ms(80.39%) && 6.8MB(100%) === //
bool judgeSquareSum(int c){
    int mid = (int)sqrt(c);
    for(int i=0; i<=mid; ++i){
        int tmp = (int) sqrt(c-i*i);
        if(tmp * tmp == c - i*i){
            return true;
        }
        if(tmp <= i){
            break;
        }
    }
    return false;
}


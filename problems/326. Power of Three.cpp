/*
=== 326. Power of Three ===

Given an integer, write a function to determine if it is a power of three.

Example 1:
    Input: 27
    Output: true
Example 2:
    Input: 0
    Output: false
Example 3:
    Input: 9
    Output: true
Example 4:
    Input: 45
    Output: false

Follow up:
    Could you do it without using any loop / recursion?
*/
// === 52ms(95.55%) & 7.7MB(23.33%) === //
bool isPowerOfThree(int n) {
    if(n<=0){
        return false;
    }
    while(n>1){
        if(n%3!=0){
            return false;
        }
        else{
            n /= 3;
        }
    }
    return true;
}
/*
=== 258. Add Digits ===

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
*/
// === 8ms(31.82%) & 6.7MB(16.67%)  === //
int addDigits(int num) {
    int ans = 0;
    while(num > 0){
        ans += num%10;
        num /= 10;
    }
    if(ans < 10){
        return ans;
    }
    else{
        return addDigits(ans);
    }
}
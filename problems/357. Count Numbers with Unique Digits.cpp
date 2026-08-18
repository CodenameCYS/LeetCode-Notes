/*
=== 357. Count Numbers with Unique Digits ===

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
    Input: 2
    Output: 91 
    - Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
                excluding 11,22,33,44,55,66,77,88,99
*/
// === 0ms(100%) && 6.7MB(100%) === //
int countNumbersWithUniqueDigits(int n){
    int flag = 9;
    int tmp = 9;
    int ans = 1;
    for(int i=1; i<=n; ++i){
        ans += tmp;
        tmp *= flag;
        -- flag;
        if(flag == 0){
            break;
        }
    }
    return ans;
}


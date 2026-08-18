/*
=== 788. Rotated Digits ===

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number N, how many numbers X from 1 to N are good?

Example:
    Input: 10
    Output: 4
    Explanation: 
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
    1. N  will be in range [1, 10000].
*/
// === 0ms(100%) && 5.2MB(100%) === //
bool is_good_digit(int i){
    return i == 2 || i == 5 || i == 6 || i == 9;
}
bool is_null_digit(int i){
    return i == 3 || i == 4 || i == 7;
}
int rotatedDigits(int N){
    int eff[10] = {0,0,0,1,1,1,2,3,3,3};
    int in_eff[10] = {0,1,2,2,2,2,2,2,2,3};
    int digits[6], size=0;
    while(N != 0){
        digits[size] = N % 10;
        N /= 10;
        ++ size;
    }
    int ans = 0;
    bool have_eff = false;
    for(int i=size-1; i>=0; --i){
        if(have_eff){
            ans += (int)((eff[digits[i]] + in_eff[digits[i]]) * pow(7, i));
        }
        else{
            ans += (int)(eff[digits[i]] * pow(7, i) + 
                         in_eff[digits[i]] * (pow(7,i) - pow(3, i)));
        }
        if(is_null_digit(digits[i])){
            break;
        }
        if(i == 0){
            if(have_eff && !is_null_digit(digits[i])){
                ++ ans;
            }
            else if(is_good_digit(digits[i])){
                ++ ans;
            }
        }
        else if(is_good_digit(digits[i])){
            have_eff = true;
        }
    }
    return ans;
}


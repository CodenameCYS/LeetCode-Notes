/*
=== 400. Nth Digit ===

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
- n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
    Input:
    3
    Output:
    3
Example 2:
    Input:
    11
    Output:
    0
    Explanation:
    The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
*/
// === 0ms(100%) && 6.7MB(100%) === //
int findNthDigit(int n){
    if(n < 10){
        return n;
    }
    long digits = 1, nums = 9;
    int have_seen = 0;
    while(n > digits * nums){
        n -= digits * nums;
        have_seen += nums;
        ++ digits;
        nums *= 10;
    }
    int num = (n + 1) / digits + have_seen;
    int digit = (digits - n % digits) % digits;
    while(digit != 0){
        num /= 10;
        -- digit;
    }
    return num % 10;
}


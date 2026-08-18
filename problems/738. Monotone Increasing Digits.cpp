/*
=== 738. Monotone Increasing Digits ===

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
    Input: N = 10
    Output: 9
Example 2:
    Input: N = 1234
    Output: 1234
Example 3:
    Input: N = 332
    Output: 299

Note: N is an integer in the range [0, 10^9].
*/
int num2digits(int n, int* digits){
    int size = 0;
    while(n != 0){
        digits[size] = n % 10;
        n /= 10;
        ++ size;
    }
    return size;
}
int digits2nums(int* digits, int size){
    int flag = 1, ans = 0;
    for(int i=0; i<size; ++i){
        ans += flag * digits[i];
        flag *= 10;
    }
    return ans;
}
bool is_monotone_increase(int* digits, int size){
    for(int i=0; i<size-1; ++i){
        if(digits[i] < digits[i+1]){
            return false;
        }
    }
    return true;
}
void change_digits(int* digits, int size){
    for(int i=0; i<size-1; ++i){
        if(is_monotone_increase(digits, size)){
            break;
        }
        digits[i] = 9;
        -- digits[i+1];
    }
    return;
}
void show(int* nums, int size){
    for(int i=0; i<size; ++i){
        printf("%d ", nums[i]);
    }
    printf("\n");
}
// === 0ms(100%) && 5.1MB(100%) === //
int monotoneIncreasingDigits(int N){
    if(N == 0){
        return 0;
    }
    int digits[10], size=0;
    size = num2digits(N, digits);
    // show(digits, size);
    change_digits(digits, size);
    // show(digits, size);
    int ans = digits2nums(digits, size);
    return ans;
}


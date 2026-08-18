/*
=== 670. Maximum Swap ===

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.
Example 2:
    Input: 9973
    Output: 9973
    Explanation: No swap.

Note:
    - The given number is in the range [0, 108]
*/
void swap_digits(int* digits, int size){
    if(size <= 1){
        return;
    }
    int max_loc = 0;
    for(int i=0; i<size-1; ++i){
        max_loc = digits[max_loc] >= digits[i] ? max_loc : i;
    }
    if(digits[max_loc] > digits[size-1]){
        int tmp = digits[max_loc];
        digits[max_loc] = digits[size-1];
        digits[size-1] = tmp;
        return;
    }
    else{
        swap_digits(digits, size-1);
    }
}
void show(int* nums, int size){
    for(int i=0; i<size; ++i){
        printf("%d", nums[i]);
    }
    printf("\n");
}
// === 0ms(100%) && 5.1MB(100%) === //
int maximumSwap(int num){
    int digits[10] = {0}, size=0;
    while(num != 0){
        digits[size] = num % 10;
        num /= 10;
        ++ size;
    }
    // show(digits, size);
    swap_digits(digits, size);
    // show(digits, size);
    int flag = 1;
    int ans = 0;
    for(int i=0; i<size; ++i){
        ans += digits[i] * flag;
        flag *= 10;
    }
    return ans;
}


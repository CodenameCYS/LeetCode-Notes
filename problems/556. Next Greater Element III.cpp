/*
=== 556. Next Greater Element III ===

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
    Input: 12
    Output: 21
Example 2:
    Input: 21
    Output: -1
*/
void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && nums[j] <= tmp){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i<j && nums[i]>=tmp){
            ++ i;
        }
        if(i<j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = tmp;
    quick_sort(nums, st, i-1);
    quick_sort(nums, i+1, ed);
}
void change_order(int* digits, int bit){
    int st = 0;
    while(digits[st] <= digits[bit+1]){
        ++ st;
    }
    int tmp = digits[bit + 1];
    digits[bit+1] = digits[st];
    digits[st] = tmp;
    quick_sort(digits, 0, bit);
}
// === 0ms(100%) && 6.8MB(100%) === //
int nextGreaterElement(int n){
    int digits[32] = {0}, size=0;
    while(n != 0){
        digits[size] = n % 10;
        n /= 10;
        ++ size;
    }
    bool need_change = false;
    int i=0;
    for(; i<size-1; ++i){
        if(digits[i] > digits[i+1]){
            need_change = true;
            break;
        }
    }
    if(need_change){
        change_order(digits, i);
        
        long ans = 0;
        long flag = 1;
        for(int j=0; j<size; ++j){
            ans += digits[j]*flag;
            flag *= 10;
        }
        return ans < INT_MAX ? ans : -1;
    }
    else{
        return -1;
    }
}


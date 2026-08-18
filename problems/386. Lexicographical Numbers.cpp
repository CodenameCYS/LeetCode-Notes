/*
=== 386. Lexicographical Numbers ===

Given an integer n, return 1 - n in lexicographical order.
For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool is_greater(int a, int b){
    int x[7], y[7];
    int x_size=0, y_size=0;
    while(a != 0){
        x[x_size] = a % 10;
        ++ x_size;
        a /= 10;
    }
    while(b != 0){
        y[y_size] = b % 10;
        ++ y_size;
        b /= 10;
    }
    while(x_size > 0 && y_size > 0){
        if(x[x_size-1] > y[y_size-1]){
            return true;
        }
        else if(x[x_size-1] < y[y_size-1]){
            return false;
        }
        else{
            -- x_size;
            -- y_size;
        }
    }
    return x_size > 0;
}

void quick_sort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp=nums[st];
    while(i<j){
        while(i<j && is_greater(nums[j], tmp)){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i<j && is_greater(tmp, nums[i])){
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
// === 364ms(5%) && 18.6MB(100%) === //
int* lexicalOrder(int n, int* returnSize){
    int* ans = (int*)malloc(n*sizeof(int));
    *returnSize = n;
    for(int i=0; i<n; ++i){
        ans[i] = i+1;
    }
    // printf("%d", is_greater(10,13));
    quick_sort(ans, 0, n-1);
    return ans;
}


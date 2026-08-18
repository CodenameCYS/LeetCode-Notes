/*
=== 628. Maximum Product of Three Numbers ===

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
    Input: [1,2,3]
    Output: 6
Example 2:
    Input: [1,2,3,4]
    Output: 24
 
Note:
    1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    2. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
*/
void add(int n, int* arr, int* size, int max_size, bool large2small){
    int s = *size + 1 < max_size ? *size + 1 : max_size;
    for(int i=0; i<s; ++i){
        if(i == *size){
            arr[i] = n;
            ++ *size;
        }
        else if(large2small){
            if(arr[i] < n){
                int tmp = arr[i];
                arr[i] = n;
                n = tmp;
            }
        }
        else{
            if(arr[i] > n){
                int tmp = arr[i];
                arr[i] = n;
                n = tmp;
            }
        }
    }
}
void show(int* nums, int s){
    for(int i=0; i<s; ++i){
        printf("%d ", nums[i]);
    }
    printf("\n");
}
// === 44ms(50%) && 7MB(100%) === //
int maximumProduct(int* nums, int numsSize){
    if(numsSize == 3){
        return nums[0]*nums[1]*nums[2];
    }
    int pos[3], s1=0;
    int neg_max[2], neg_min[3], s2=0, s3=0;
    for(int i=0; i<numsSize; ++i){
        if(nums[i] >= 0){
            add(nums[i], pos, &s1, 3, true);
        }
        else{
            add(nums[i], neg_max, &s2, 2, false);
            add(nums[i], neg_min, &s3, 3, true);
        }
    }
    if(s1 == 0){
        return neg_min[0] * neg_min[1] * neg_min[2];
    }
    else if(s1 < 3){
        return neg_max[0] * neg_max[1] * pos[0];
    }
    else{
        int tmp = pos[1] * pos[2];
        if(s2 == 2){
            tmp = neg_max[0] * neg_max[1] > tmp ? neg_max[0] * neg_max[1] : tmp;
        }
        return tmp * pos[0];
    }
}


/*
=== 414. Third Maximum Number ===

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
    Input: [3, 2, 1]
    Output: 1
    - Explanation: The third maximum is 1.
Example 2:
    Input: [1, 2]
    Output: 2
    - Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
    Input: [2, 2, 3, 1]
    Output: 1
    - Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.
*/
void insert_num(int* nums, int* size, int max_size, int val){
    for(int i=0; i<*size; ++i){
        if(nums[i] == val){
            return;
        }
    }
    if(*size == 0){
        nums[*size] = val;
        ++ *size;
    }
    else if(nums[*size-1] > val){
        if(*size < max_size){
            nums[*size] = val;
            ++ *size;
        }
    }
    else{
        int flag = *size-1;
        while(flag >= 0 && nums[flag] < val){
            -- flag;
        }
        ++ flag;
        if(*size < max_size){
            ++ *size;
        }
        int present = val;
        while(flag < *size){
            int tmp = nums[flag];
            nums[flag] = present;
            present = tmp;
            ++ flag;
        }
    }
}

void show(int* nums, int size){
    for(int i=0; i<size; ++i){
        printf("%d\t", nums[i]);
    }
    printf("\n");
}
// === 4ms(92.86%) && 7.4MB(100%) === //
int thirdMax(int* nums, int numsSize){
    int top3[3];
    int size = 0;
    for(int i=0; i < numsSize; ++i){
        insert_num(top3, &size, 3, nums[i]);
        // show(top3, size);
    }
    if(size < 3){
        return top3[0];
    }
    else{
        return top3[2];
    }
}


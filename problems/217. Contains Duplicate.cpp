/*
=== 217. Contains Duplicate ===

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
    Input: [1,2,3,1]
    Output: true

Example 2:
    Input: [1,2,3,4]
    Output: false

Example 3:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
*/
// === 924 ms === //
bool QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return false;
    }
    int temp = nums[st];
    int i=st, j=ed;
    while(i<j){
        while(i<j && nums[j]>temp){
            --j;
        }
        if(i<j){
            if(nums[j] == temp){
                return true;
            }
            else{
                nums[i] = nums[j];
            }
            ++i;
        }
        while(i<j && nums[i]<temp){
            ++i;
        }
        if(i<j){
            if(nums[i] == temp){
                return true;
            }
            else{
                nums[j] = nums[i];
            }
            --j;
        }
    }
    nums[i] = temp;
    return QuickSort(nums, st, i-1) || QuickSort(nums, i+1, ed);
}
bool containsDuplicate(int* nums, int numsSize) {
    return QuickSort(nums, 0, numsSize-1);
}
/* ====================================================================================== */
// === 956 ms === //
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int temp = nums[st];
    int i=st, j=ed;
    while(i<j){
        while(i<j && nums[j]>=temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i]<temp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
bool containsDuplicate(int* nums, int numsSize) {
    QuickSort(nums, 0, numsSize-1);
    int memory = nums[0];
    for(int i=1; i<numsSize; ++i){
        if(nums[i] == memory){
            return true;
        }
        else{
            memory = nums[i];
        }
    }
    return false;
}
/* =========================================================================================== */
// === 8ms === //
int comp(const void *a,const void *b){
    return *(int*)a-*(int*)b;
}
bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums,numsSize,sizeof(int),comp);
    for(int i=0;i<numsSize-1;i++){
        if(nums[i]==nums[i+1]){
            return true;
        }
    }
    return false;
}
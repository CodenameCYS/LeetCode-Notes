/*
=== 41. First Missing Positive ===

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
*/
void QuickSort(int* nums, int start, int end){
    if(start >= end){
        return;
    }
    
    int i = start, j = end;
    int temp = nums[start];
    while(i < j){
        while(i < j && nums[j] >= temp){
            --j;
        }
        if(i < j){
            nums[i] = nums[j];
            ++i;
        }
        while(i < j && nums[i] <= temp){
            ++i;
        }
        if(i < j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, start, i-1);
    QuickSort(nums, i+1, end);
    return;
}

int firstMissingPositive(int* nums, int numsSize) {
    QuickSort(nums, 0, numsSize-1);
    
    int loc = 0;
    while(nums[loc] <= 0){
        ++loc;
    }
    if(nums[loc] > 1){
        return 1;
    }
    
    for(int i=loc; i<numsSize; ++i){
        if(nums[i] - nums[i-1] > 1 && nums[i-1] >= 0){
            return nums[i-1] + 1;
        }
    }
    
    return nums[numsSize-1] + 1;
}

/*
=== The Right Answer ===

// 这段代码存在问题，无法解决[3,4,-1,1]这样的问题，因为在交换的过程中把1交换到前面去了，没发正确放到A[0]位置；

class Solution
{
public:
    int firstMissingPositive(int A[], int n)
    {
        for(int i = 0; i < n; ++ i)
            while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i < n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};

=== 修正为下述代码 ===
int firstMissingPositive(int* nums, int numsSize) {
    int loc = 0;
    while(loc < numsSize){
        if(nums[loc] > 0 && nums[loc] <= numsSize && nums[nums[loc]-1] != nums[loc]){
            int temp = nums[loc];
            nums[loc] = nums[temp-1];
            nums[temp-1] = temp;
        }
        else{
            ++loc;
        }
    }
    
    for(int i=0; i<numsSize; ++i){
        if(nums[i] != i+1){
            return i+1;
        }
    }
    
    return nums[numsSize-1] + 1;
}

## 测试得到击败93.36%的人 ##

*/
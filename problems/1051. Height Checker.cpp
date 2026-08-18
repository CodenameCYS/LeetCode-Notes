/*
=== 1051. Height Checker ===

Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Example 1:
    Input: [1,1,4,2,1,3]
    Output: 3
    - Explanation: 
    Students with heights 4, 3 and the last 1 are not standing in the right positions.
 
Note:
    1. 1 <= heights.length <= 100
    2. 1 <= heights[i] <= 100
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed;
    int temp = nums[st];
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
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
// === 0ms && 7.1MB === //
int heightChecker(int* heights, int heightsSize){
    int sorted[heightsSize];
    for(int i=0; i<heightsSize; ++i){
        sorted[i]= heights[i];
    }
    QuickSort(sorted, 0, heightsSize-1);
    
    int ans=0;
    for(int i=0; i<heightsSize; ++i){
        if(heights[i] != sorted[i]){
            ++ ans;
        }
    }
    return ans;
}


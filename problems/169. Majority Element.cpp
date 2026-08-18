/*
=== 169. Majority Element ===

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
*/
# include <stdio.h>
# include <stdlib.h>
# include <vector>

using namespace std;

// === ver1.0 === //
// beat 5.03% //
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

int majorityElement(int* nums, int numsSize) {
    QuickSort(nums, 0, numsSize-1);
    return nums[numsSize/2];
}

// === ver2.0 === //
// copied from others, beat 98.71% //
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major=nums[0], count = 1;
        for(int i=1; i<nums.size();i++){
            if(count==0){
                count++;
                major=nums[i];
            }else if(major==nums[i]){
                count++;
            }else count--;
            
        }
        return major;
    }
};
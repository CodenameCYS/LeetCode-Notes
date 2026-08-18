/*
=== 16. 3Sum Closest ===

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int tmp = nums[st];
    int i=st, j=ed;
    while(i<j){
        while(i<j && nums[j] >= tmp){
            -- j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++ i;
        }
        while(i<j && nums[i] <= tmp){
            ++ i;
        }
        if(i<j){
            nums[j] = nums[i];
            -- j;
        }
    }
    nums[i] = tmp;
    QuickSort(nums, st, i-1);
    QuickSort(nums, i+1, ed);
}
// === 0ms(100%) && 7.2MB(100%) === //
int threeSumClosest(int* nums, int numsSize, int target){
    QuickSort(nums, 0, numsSize-1);
    int ans = nums[0] + nums[1] + nums[2];
    int i = 0;
    while(i<numsSize-2){
        int a = nums[i];
        int j = i+1, k = numsSize-1;
        while(j<k){
            int b = nums[j], c= nums[k];
            if(a + b + c == target){
                return target;
            }
            else{
                int tmp = a + b + c;
                ans = abs(tmp - target) < abs(ans - target) ? tmp : ans;
            }
            if(a+b+c > target){
                while(j<k && nums[k] == c){
                    -- k;
                }
            }
            else{
                while(j<k && nums[j] == b){
                    ++ j;
                }
            }
        }
        while(i<numsSize-2 && nums[i] == a){
            ++ i;
        }
    }
    return ans;
}


/*
=== 209. Minimum Size Subarray Sum ===

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
*/
int minSubArrayLen(int s, int* nums, int numsSize) {
    if(numsSize == 0){
        return 0;
    }
    int st=0, ed = 1;
    int sum = nums[0];
    int ans = 0;
    while(true){
        while(ed < numsSize && sum < s){
            sum += nums[ed];
            ++ ed;
        }
        if(sum < s){
            break;
        }
        int temp = ed-st;
        if(ans == 0){
            ans = temp;
        }
        else{
            ans = ans <= temp ? ans : temp;
        }
        
        while(st < ed && sum >= s){
            sum -= nums[st];
            ++st;
        }
        temp = ed-st+1;
        ans = ans <= temp ? ans : temp;
    }
    return ans;
}
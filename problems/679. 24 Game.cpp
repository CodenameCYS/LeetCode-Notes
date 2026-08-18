/*
=== 679. 24 Game ===

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
    Input: [4, 1, 8, 7]
    Output: True
    Explanation: (8-4) * (7-1) = 24
Example 2:
    Input: [1, 2, 1, 2]
    Output: False

Note:
    1. The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    2. Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    3. You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
*/
bool judge_point_24(double* nums, int numsSize){
    if(numsSize == 1){
        return fabs(nums[0] - 24) < 1e-6;
    }
    for(int i=0; i<numsSize-1; ++i){
        for(int j=i+1; j<numsSize; ++j){
            double n[numsSize-1];
            int size=0;
            for(int k=0; k<numsSize; ++k){
                if(k != i && k != j){
                    n[size] = nums[k];
                    ++ size;
                }
            }
            bool tmp = false;
            n[numsSize-2] = nums[i] + nums[j];
            tmp = tmp || judge_point_24(n, numsSize-1);
            n[numsSize-2] = nums[i] - nums[j];
            tmp = tmp || judge_point_24(n, numsSize-1);
            n[numsSize-2] = - nums[i] + nums[j];
            tmp = tmp || judge_point_24(n, numsSize-1);
            n[numsSize-2] = nums[i] * nums[j];
            tmp = tmp || judge_point_24(n, numsSize-1);
            n[numsSize-2] = nums[i] / nums[j];
            tmp = tmp || judge_point_24(n, numsSize-1);
            n[numsSize-2] = nums[j] / nums[i];
            tmp = tmp || judge_point_24(n, numsSize-1);
            if(tmp){
                return true;
            }
        }
    }
    return false;
}
// === 0ms(100%) && 5.4MB(100%) === //
bool judgePoint24(int* nums, int numsSize){
    double n[numsSize];
    for(int i=0; i<numsSize; ++i){
        n[i] = (double)nums[i];
    }
    return judge_point_24(n, numsSize);
}


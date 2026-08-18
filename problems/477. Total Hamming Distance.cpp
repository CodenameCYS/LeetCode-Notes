/*
=== 477. Total Hamming Distance ===

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
    Input: 4, 14, 2
    Output: 6
    Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
    showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
    1. Elements of the given array are in the range of 0 to 10^9
    2. Length of the array will not exceed 10^4.
*/
// === 48ms(27.03%) && 8MB(66.67%) === //
int totalHammingDistance(int* nums, int numsSize){
    int ans = 0;
    while(true){
        long sum = 0;
        int zero = 0, one = 0;
        for(int i=0; i<numsSize; ++i){
            if(nums[i] % 2 == 0){
                ++ zero;
            }
            else{
                ++ one;
            }
            nums[i] /= 2;
            sum += nums[i];
        }
        ans += one*zero;
        if(sum == 0){
            break;
        }
    }
    return ans;
}


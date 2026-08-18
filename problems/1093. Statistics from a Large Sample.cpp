/*
=== 1093. Statistics from a Large Sample ===

We sampled integers between 0 and 255, and stored the results in an array count:  count[k] is the number of integers we sampled equal to k.
Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers.  The mode is guaranteed to be unique.
(Recall that the median of a sample is:
    - The middle element, if the elements of the sample were sorted and the number of elements is odd;
    - The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.)
 
Example 1:
    Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Example 2:
    Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,4.00000,2.18182,2.00000,1.00000]

Constraints:
    1. count.length == 256
    2. 1 <= sum(count) <= 10^9
    3. The mode of the sample that count represents is unique.
    4. Answers within 10^-5 of the true value will be accepted as correct.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 0ms && 7MB === //
double* sampleStats(int* count, int countSize, int* returnSize){
    double* ans = (double*)malloc(5*sizeof(double));
    ans[0] = -1;
    *returnSize = 5;
    
    int num = 0;
    double sum = 0;
    int mode = -1;
    for(int i=0; i<256; i++){
        if(count[i] > 0){
            ans[0] = ans[0] == -1 ? i : ans[0];
            ans[1] = i;
            num += count[i];
            sum += i*count[i];
            
            if(mode == -1 || count[i] > count[mode]){
                mode = i;
            }
        }
    }
    if(num == 0){
        ans[0] = 0;
        ans[1] = 0;
        ans[2] = 0;
        ans[3] = 0;
        ans[4] = 0;
    }
    else{
        ans[2] = sum / num;
        ans[4] = mode;
    }
    int n1 = (num + 1) / 2;
    int n2 = (num + 2) / 2;
    double a1=-1, a2=-1;
    num = 0;
    for(int i=0; i<256; ++i){
        num += count[i];
        if(num >= n1){
            a1 = a1 == -1 ? i : a1;
        }
        if(num >= n2){
            a2 = a2 == -1 ? i : a2;
        }
    }
    ans[3] = (a1 + a2) / 2;
    return ans;
}


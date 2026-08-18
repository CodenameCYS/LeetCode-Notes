/*
=== 274. H-Index ===

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:
    Input: citations = [3,0,6,1,5]
    Output: 3 
- Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
*/
// === 4ms(60%) & 7.6MB(100%) === //
void QuickSort(int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, temp=nums[st];
    while(i<j){
        while(i<j && nums[j]>=temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            ++i;
        }
        while(i<j && nums[i]<=temp){
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
int hIndex(int* citations, int citationsSize) {
    QuickSort(citations, 0, citationsSize-1);
    for(int i=0; i<citationsSize; ++i){
        if(citations[i] >= citationsSize-i){
            return citationsSize-i;
        }
    }
    return 0;
}
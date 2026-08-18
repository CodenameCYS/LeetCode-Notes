/*
=== 945. Minimum Increment to Make Array Unique ===
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
Return the least number of moves to make every value in A unique.

Example 1:
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 
Note:
1. 0 <= A.length <= 40000
2. 0 <= A[i] < 40000
*/
bool QuickSort(int* seq, int start, int end){
    if(end <= start){
        return true;
    }
    int i=start, j=end;
    int temp = seq[start];
    while(i < j){
        while(i<j && seq[j]>=temp){
            --j;
        }
        if(i<j){
            seq[i] = seq[j];
            ++i;
        }
        while(i<j && seq[i]<=temp){
            ++i;
        }
        if(i<j){
            seq[j] = seq[i];
            --j;
        }
    }
    seq[i] = temp;
    QuickSort(seq, start, i-1);
    QuickSort(seq, i+1, end);
    return true;
}
int minIncrementForUnique(int* A, int ASize) {
    if(ASize <= 1){
        return 0;
    }
    QuickSort(A, 0, ASize-1);
    /*
    for(int i=0; i<ASize; ++i){
        printf("%d\t", A[i]);
    }
    printf("\n");
    */
    int ans = 0;
    int val = A[0] + 1;
    for(int i=1; i<ASize; ++i){
        if(A[i] < val){
            ans += val - A[i];
            val = val + 1;
        }
        else{
            val = A[i] + 1;
        }
    }
    return ans;
}
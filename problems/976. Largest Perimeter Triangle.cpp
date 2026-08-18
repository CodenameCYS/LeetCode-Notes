/*
=== 976. Largest Perimeter Triangle ===

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.

Example 1:
    Input: [2,1,2]
    Output: 5
Example 2:
    Input: [1,2,1]
    Output: 0
Example 3:
    Input: [3,2,3,4]
    Output: 10
Example 4:
    Input: [3,6,2,3]
    Output: 8
 
Note:
    1. 3 <= A.length <= 10000
    2. 1 <= A[i] <= 10^6
*/
// === 20ms === //
void QuickSort(int* seq, int start, int end){
    if(end <= start){
        return;
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
    return;
}

int largestPerimeter(int* A, int ASize) {
    QuickSort(A, 0, ASize-1);
    for(int i=ASize-3; i>=0; --i){
        if(A[i] + A[i+1] > A[i+2]){
            return A[i] + A[i+1] + A[i+2];
        }
    }
    return 0;
}
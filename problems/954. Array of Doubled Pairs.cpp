/*
=== 954. Array of Doubled Pairs ===

Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

Example 1:
Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false

Example 3:
Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
Input: [1,2,4,16,8,4]
Output: false
 
Note:
1. 0 <= A.length <= 30000
2. A.length is even
3. -100000 <= A[i] <= 100000
*/
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
void SplitData(int* A, int ASize, int* dataset1, int* dataset1_size, int* dataset2, int* dataset2_size){
    *dataset1_size = 0;
    *dataset2_size = 0;
    for(int i=0; i<ASize; ++i){
        if(A[i] >= 0){
            dataset1[(*dataset1_size)] = A[i];
            ++ *dataset1_size;
        }
        else{
            dataset2[(*dataset2_size)] = A[i];
            ++ *dataset2_size;
        }
    }
    return;
}
bool canReorder(int* A, int ASize, bool state){
    if(ASize == 0){
        return true;
    }
    bool isUsed[ASize];
    for(int i=0; i<ASize; ++i){
        isUsed[i] = false;
    }
    if(state){
        int small = 0, large = 1;
        while(large < ASize && small < ASize){
            isUsed[small] = true;
            while(large < ASize && (isUsed[large] || A[large] != 2*A[small])){
                ++ large;
            }
            if(large >= ASize){
                return false;
            }
            else{
                isUsed[large] = true;
                ++ large;
            }
            while(small < ASize && isUsed[small]){
                ++ small;
            }
        }
        return small >= ASize && large >= ASize;
    }
    else{
        int small = ASize-1, large = ASize-2;
        while(large >= 0 && small >= 0){
            isUsed[small] = true;
            while(large >= 0 && (isUsed[large] || A[large] != 2*A[small])){
                -- large;
            }
            if(large < 0){
                return false;
            }
            else{
                isUsed[large] = true;
                -- large;
            }
            while(small >= 0 && isUsed[small]){
                -- small;
            }
        }
        return small<0 && large<0;
    }
}

bool canReorderDoubled(int* A, int ASize) {
    int positive[30000], negative[30000];
    int positive_num, negative_num;
    SplitData(A, ASize, positive, &positive_num, negative, &negative_num);
    if(positive_num % 2 != 0){
        return false;
    }
    
    QuickSort(positive, 0, positive_num-1);
    QuickSort(negative, 0, negative_num-1);
    
    return canReorder(positive, positive_num, true) && canReorder(negative, negative_num, false);
}
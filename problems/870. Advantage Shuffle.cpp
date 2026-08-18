/*
=== 870. Advantage Shuffle ===

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B.

Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:
1. 1 <= A.length = B.length <= 10000
2. 0 <= A[i] <= 10^9
3. 0 <= B[i] <= 10^9
*/

# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int* advantageCount(int* A, int ASize, int* B, int BSize, int* returnSize);
void QuickSort(int *vec, int *seq, int start, int end);
void TestQuickSort(int len);
void TestadvantageCount(int len);

int main(){

    //TestQuickSort(10);

    TestadvantageCount(10);

    system("pause");
    return 1;
}

void QuickSort(int *vec, int *seq, int start, int end){
    if(start >= end){
        return;
    }
    
    int i = start, j = end;
    int temp = vec[start], tempseq = seq[start];
    while(i < j){
        while(i < j && vec[j] > temp){
            --j;
        }
        if(i < j){
            vec[i] = vec[j];
            seq[i] = seq[j];
            ++i;
        }
        while(i < j && vec[i] < temp){
            ++i;
        }
        if(i < j){
            vec[j] = vec[i];
            seq[j] = seq[i];
            --j;
        }
    }
    vec[i] = temp;
    seq[i] = tempseq;

    QuickSort(vec, seq, start, i-1);
    QuickSort(vec, seq, i+1, end);

    return;
}

void TestQuickSort(int len){
    srand((unsigned int)time(NULL));

    int A[len], B[len], seqa[len], seqb[len];
    for(int i=0; i<len; ++i){
        A[i] = rand()/32767.0*100;
        B[i] = rand()/32767.0*100;
        seqa[i] = i;
        seqb[i] = i;
    }
    printf("A:\t");
    for(int i=0; i<len; ++i){
        printf("%d:%d\t",seqa[i], A[i]);
    }
    printf("\n");
    printf("B:\t");
    for(int i=0; i<len; ++i){
        printf("%d:%d\t",seqb[i], B[i]);
    }
    printf("\n");

    QuickSort(A, seqa, 0, len-1);
    QuickSort(B, seqb, 0, len-1);

    printf("A:\t");
    for(int i=0; i<len; ++i){
        printf("%d:%d\t",seqa[i], A[i]);
    }
    printf("\n");
    printf("B:\t");
    for(int i=0; i<len; ++i){
        printf("%d:%d\t",seqb[i], B[i]);
    }
    printf("\n");
}

int* advantageCount(int* A, int ASize, int* B, int BSize, int* returnSize) {
    if(ASize != BSize){
        printf("A & B are not equal size.\n");
        return NULL;
    }

    *returnSize = ASize;

    int* ans = (int *)malloc(ASize * sizeof(int));
    int a[ASize], b[BSize], seqa[ASize], seqb[BSize], taga[ASize], tagb[BSize];
    for(int i = 0; i < ASize ; ++i){
        seqa[i] = i,    seqb[i] = i;
        a[i] = A[i],    b[i] = B[i];
        ans[i] = 0;
        taga[i] = 0,    tagb[i] = 0;
    }

    QuickSort(a, seqa, 0, ASize-1);
    QuickSort(b, seqb, 0, BSize-1);

    int i = 0, j = 0;
    while(i < ASize && j < BSize){
        if(a[i] > b[j]){
            ans[seqb[j]] = a[i];
            tagb[seqb[j]] = 1;
            taga[i] = 1;
            ++i;
            ++j;
        }
        else{
            ++i;
        }
    }

    i = 0, j = 0;
    while(i < ASize && j < BSize){
        if(tagb[i] == 1){
            ++i;
            continue;
        }
        else{
            while(taga[j] == 1){
                ++j;
            }
            ans[i] = a[j];
            ++i;
            ++j;
        }
    }

    return ans;
}

void TestadvantageCount(int len){
    srand((unsigned int)time(NULL));

    int A[len], B[len], returnSize;

    printf("A:\t");
    for(int i=0; i<len; ++i){
        A[i] = rand()/32767.0*100;
        printf("%d\t", A[i]);
    }
    printf("\n");

    printf("B:\t");
    for(int i=0; i<len; ++i){
        B[i] = rand()/32767.0*100;
        printf("%d\t", B[i]);
    }
    printf("\n");

    int *ans = advantageCount(A, len, B, len, &returnSize);

    printf("ans:\t");
    for(int i=0; i<returnSize; ++i){
        printf("%d\t",ans[i]);
    }
    printf("\n");
}
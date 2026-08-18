/*
=== 986. Interval List Intersections ===

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
    Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 
Note:
    1. 0 <= A.length < 1000
    2. 0 <= B.length < 1000
    3. 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
*/

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 12 ms & 1MB === //
struct Interval* intervalIntersection(struct Interval* A, int ASize, struct Interval* B, int BSize, int* returnSize) {
    struct Interval* ans = (struct Interval*)malloc((ASize + BSize) * sizeof(struct Interval));
    *returnSize = 0;
    
    int aloc = 0, bloc = 0;
    while(aloc < ASize && bloc < BSize){
        if(A[aloc].start <= B[bloc].start && B[bloc].start <= A[aloc].end){
            if(A[aloc].end < B[bloc].end){
                ans[*returnSize].start = B[bloc].start;
                ans[*returnSize].end = A[aloc].end;
                ++ *returnSize;
                ++ aloc;
            }
            else{
                ans[*returnSize].start = B[bloc].start;
                ans[*returnSize].end = B[bloc].end;
                ++ *returnSize;
                ++ bloc;
            }
        }
        else if(A[aloc].end < B[bloc].start){
            ++ aloc;
        }
        else if(B[bloc].end < A[aloc].start){
            ++ bloc;
        }
        else{
            if(B[bloc].end < A[aloc].end){
                ans[*returnSize].start = A[aloc].start;
                ans[*returnSize].end = B[bloc].end;
                ++ *returnSize;
                ++ bloc;
            }
            else{
                ans[*returnSize].start = A[aloc].start;
                ans[*returnSize].end = A[aloc].end;
                ++ *returnSize;
                ++ aloc;
            }
        }
    }
    
    return ans;
}
/*
=== 973. K Closest Points to Origin ===

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
Explanation: 
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:
    1. 1 <= K <= points.length <= 10000
    2. -10000 < points[i][0] < 10000
    3. -10000 < points[i][1] < 10000
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
// === 316 ms === //
int findMax(int** points, int size){
    if(size <= 1){
        return 0;
    }
    long max_distance = points[0][0]*points[0][0] + points[0][1]*points[0][1];
    int ans = 0;
    for(int i=1; i<size; ++i){
        long temp = points[i][0]*points[i][0] + points[i][1]*points[i][1];
        if(temp > max_distance){
            ans = i;
            max_distance = temp;
        }
    }
    return ans;
}
int** kClosest(int** points, int pointsRowSize, int *pointsColSizes, int K, int** columnSizes, int* returnSize) {
    int** ans = (int**)malloc(K*sizeof(int*));
    *columnSizes = (int*)malloc(K*sizeof(int));
    *returnSize = 0;
    int max_loc = -1;
    long max_distance = -1;
    for(int i=0; i<pointsRowSize; ++i){
        if(i<K){
            ans[(*returnSize)] = (int*)malloc(2*sizeof(int));
            ans[(*returnSize)][0] = points[i][0];
            ans[(*returnSize)][1] = points[i][1];
            columnSizes[0][i] = 2;
            ++ *returnSize;
        }
        else{
            if(max_loc == -1){
                max_loc = findMax(ans, *returnSize);
                max_distance = ans[max_loc][0]*ans[max_loc][0] + ans[max_loc][1]*ans[max_loc][1];
            }
            long temp_distance = points[i][0]*points[i][0] + points[i][1]*points[i][1];
            if(temp_distance < max_distance){
                ans[max_loc][0] = points[i][0];
                ans[max_loc][1] = points[i][1];
                max_loc = findMax(ans, *returnSize);
                max_distance = ans[max_loc][0]*ans[max_loc][0] + ans[max_loc][1]*ans[max_loc][1];
            }
        }
    }
    return ans;
}
// ========================================================================================================================= //
// === 80 ms === //
long distance(int* point){
    return point[0]*point[0] + point[1]*point[1];
}
void QuickSort(int** points, int st, int ed){
    if(st >= ed){
        return;
    }
    int* temp[2];
    temp[0] = points[st][0], temp[1] = points[st][1];
    long pivot = distance(points[st]);
    int i=st, j=ed;
    while(i<j){
        while(i<j && distance(points[j]) >= pivot){
            --j;
        }
        if(i<j){
            points[i][0] = points[j][0];
            points[i][1] = points[j][1];
            ++i;
        }
        while(i<j && distance(points[i]) <= pivot){
            ++i;
        }
        if(i<j){
            points[j][0] = points[i][0];
            points[j][1] = points[i][1];
            --j;
        }
    }
    points[i][0] = temp[0], points[i][1] = temp[1];
    QuickSort(points, st, i-1);
    QuickSort(points, i+1, ed);
    return;
}
int** kClosest(int** points, int pointsRowSize, int *pointsColSizes, int K, int** columnSizes, int* returnSize) {
    QuickSort(points, 0, pointsRowSize-1);

    int** ans = (int**)malloc(K*sizeof(int*));
    *columnSizes = (int*)malloc(K*sizeof(int));
    *returnSize = K;
    for(int i=0; i<K; ++i){
        ans[i] = (int*)malloc(2*sizeof(int));
        columnSizes[0][i] = 2;
        ans[i][0] = points[i][0], ans[i][1] = points[i][1];
    }
    return ans;
}
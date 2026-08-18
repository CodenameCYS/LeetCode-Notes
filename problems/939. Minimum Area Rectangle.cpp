/*
=== 939. Minimum Area Rectangle ===

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 
Note:
1. 1 <= points.length <= 500
2. 0 <= points[i][0] <= 40000
3. 0 <= points[i][1] <= 40000
4. All points are distinct.
*/
int minAreaRect(int** points, int pointsRowSize, int *pointsColSizes) {
    int ans = 0;
    for(int i=0; i<pointsRowSize; ++i){
        for(int j=i+1; j<pointsRowSize; ++j){
            if(points[i][0] == points[j][0] || points[i][1] == points[j][1]){
                continue;
            }
            int x1 = points[i][0], x2 = points[j][0], y1 = points[i][1], y2 = points[j][1];
            bool s1 = false, s2 = false;
            for(int k=i+1; k<pointsRowSize; ++k){
                if(points[k][0] == x1 && points[k][1] == y2){
                    s1 = true;
                }
                if(points[k][0] == x2 && points[k][1] == y1){
                    s2 = true;
                }
                if(s1 && s2){
                    if(ans == 0){
                        ans = abs((x2-x1)*(y2-y1));
                    }
                    else{
                        int size = abs((x2-x1)*(y2-y1));
                        ans = ans <= size? ans: size;
                    }
                    break;
                }
            }
        }
    }
    return ans;
}
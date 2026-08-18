/*
=== 963. Minimum Area Rectangle II ===

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.
If there isn't any rectangle, return 0.

Example 1:
    Input: [[1,2],[2,1],[1,0],[0,1]]
    Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:
    Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
    Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:
    Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
    Output: 0
Explanation: There is no possible rectangle to form from these points.

Example 4:
    Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
    Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 
Note:
    1. 1 <= points.length <= 50
    2. 0 <= points[i][0] <= 40000
    3. 0 <= points[i][1] <= 40000
    4. All points are distinct.
    5. Answers within 10^-5 of the actual value will be accepted as correct.
*/
// === 16ms === //
bool isperpendicular(int* point1, int* point2, int* point3, int* point4){
    double x1=point1[0], x2=point2[0], x3=point3[0], x4=point4[0];
    double y1=point1[1], y2=point2[1], y3=point3[1], y4=point4[1];
    if(x1 == x2){
        if(y3 == y4){
            return true;
        }
        else{
            return false;
        }
    }
    else if(x3 == x4){
        if(y1 == y2){
            return true;
        }
        else{
            return false;
        }
    }
    else if((y2-y1)*(y4-y3)/((x4-x3)*(x2-x1)) == -1){
        return true;
    }
    else{
        return false;
    }
}

double findMinRect(int* point1, int* point2, int** points, int pointsnum){
    double ans = 0, temp;
    double x1 = point1[0], y1 = point1[1], x2 = point2[0], y2 = point2[1];
    for(int i=0; i<pointsnum-1; ++i){
        double x3 = points[i][0], y3 = points[i][1];
        // printf("(%2.0f,%2.0f)\t(%2.0f,%2.0f)\t(%2.0f,%2.0f)\n", x1,y1,x2,y2,x3,y3);
        if(isperpendicular(point1, point2, point1, points[i])){
            // printf("(%2.0f,%2.0f)\t(%2.0f,%2.0f)\t(%2.0f,%2.0f)\n", x1,y1,x2,y2,x3,y3);
            for(int j=i+1; j<pointsnum; ++j){
                if(points[j][0]==x2+x3-x1 && points[j][1]==y2+y3-y1){
                    // printf("matched pattern 01:\t(%d,%d)\n",points[j][0],points[j][1]);
                    temp = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) * sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
                    if(ans == 0){
                        ans = temp;
                    }
                    else{
                        ans = ans <= temp ? ans : temp;
                    }
                }
            }
        }
        else if(isperpendicular(point2, point1, point2, points[i])){
            // printf("(%2.0f,%2.0f)\t(%2.0f,%2.0f)\t(%2.0f,%2.0f)\n", x1,y1,x2,y2,x3,y3);
            for(int j=i+1; j<pointsnum; ++j){
                if(points[j][0]==x1+x3-x2 && points[j][1]==y1+y3-y2){
                    // printf("matched pattern 02:\t(%d,%d)\n",points[j][0],points[j][1]);
                    temp = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) * sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
                    if(ans == 0){
                        ans = temp;
                    }
                    else{
                        ans = ans <= temp ? ans : temp;
                    }
                }
            }
        }
        else if(isperpendicular(points[i], point1, points[i], point2)){
            // printf("(%2.0f,%2.0f)\t(%2.0f,%2.0f)\t(%2.0f,%2.0f)\n", x1,y1,x2,y2,x3,y3);
            for(int j=i+1; j<pointsnum; ++j){
                if(points[j][0]==x1+x2-x3 && points[j][1]==y1+y2-y3){
                    // printf("matched pattern 03:\t(%d,%d)\n",points[j][0],points[j][1]);
                    temp = sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1)) * sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
                    if(ans == 0){
                        ans = temp;
                    }
                    else{
                        ans = ans <= temp ? ans : temp;
                    }
                }
            }
        }
    }
    return ans;
}

double minAreaFreeRect(int** points, int pointsRowSize, int *pointsColSizes) {
    double ans = 0;
    for(int i=0; i<pointsRowSize-3; ++i){
        for(int j=i+1; j<pointsRowSize-2; ++j){
            double tempmin = findMinRect(points[i], points[j], &points[j+1], pointsRowSize-j-1);
            if(ans == 0){
                ans = tempmin;
            }
            else if(tempmin != 0){
                ans = tempmin < ans ? tempmin : ans;
            }
        }
    }
    return ans;
}
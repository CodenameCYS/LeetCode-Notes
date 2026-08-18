/*
=== 812. Largest Triangle Area ===

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2
    Explanation: 
    The five points are show in the figure below. The red triangle is the largest.

Notes:
    1. 3 <= points.length <= 50.
    2. No points will be duplicated.
    3. -50 <= points[i][j] <= 50.
    4. Answers within 10^-6 of the true value will be accepted as correct.
*/
double area(int* p1, int* p2, int* p3){
    return 0.5*abs(p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[0]*p3[1]-p2[0]*p1[1]-p3[0]*p2[1]);
}
// === 4ms(100%) && 5.5MB(100%) === //
double largestTriangleArea(int** points, int pointsSize, int* pointsColSize){
    double ans = 0;
    for(int i=0; i<pointsSize-2; ++i){
        for(int j=i+1; j<pointsSize-1; ++j){
            for(int k=j+1; k<pointsSize; ++k){
                double s = area(points[i], points[j], points[k]);
                // printf("(%d, %d),(%d, %d),(%d, %d) -> %lf\n", points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1], s);
                ans = ans > s ? ans : s;
            }
        }
    }
    return ans;
}


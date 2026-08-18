/*
=== 1232. Check If It Is a Straight Line ===

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false
 
Constraints:
    1. 2 <= coordinates.length <= 1000
    2. coordinates[i].length == 2
    3. -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    4. coordinates contains no duplicate point.
*/
// === 8ms & 7.9MB === //
bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize){
    if(coordinates[0][0] == coordinates[1][0]){
        for(int i=2; i<coordinatesSize; ++i){
            if(coordinates[i][0] != coordinates[0][0]){
                return false;
            }
        }
    }
    else if(coordinates[0][1] == coordinates[1][1]){
        for(int i=2; i<coordinatesSize; ++i){
            if(coordinates[i][1] != coordinates[0][1]){
                return false;
            }
        }
    }
    else{
        double k = 1.0*(coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]);
        double b = coordinates[0][1] - k*coordinates[0][0];
        double epsilon = 1e-6;
        for(int i=2; i<coordinatesSize; ++i){
            if(fabs(coordinates[i][1] - k*coordinates[i][0]-b) > epsilon){
                return false;
            }
        }
    }
    return true;
}


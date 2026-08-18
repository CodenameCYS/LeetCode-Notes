/*
=== 593. Valid Square ===

Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True
 
Note:
    1. All the input integers are in the range [-10000, 10000].
    2. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    3. Input points have no order.
*/
// === 4ms(53.85%) && 6.7MB(66.67%) === //
bool is_square(int* p0, int* p1, int* p2, int* p3){
    if(
        (p1[0]-p0[0])*(p2[0]-p0[0]) + (p1[1]-p0[1])*(p2[1]-p0[1]) == 0 
        && (p3[0]-p2[0] == p1[0]-p0[0] && p3[1]-p2[1] == p1[1]-p0[1])
        && (p3[0]-p2[0])*(p3[0]-p2[0]) + (p3[1]-p2[1])*(p3[1]-p2[1]) == 
           (p3[0]-p1[0])*(p3[0]-p1[0]) + (p3[1]-p1[1])*(p3[1]-p1[1])
        && (p3[0]-p2[0])*(p3[0]-p2[0]) + (p3[1]-p2[1])*(p3[1]-p2[1]) != 0
    ){
        return true;
    }
    return false;
}
bool validSquare(int* p1, int p1Size, int* p2, int p2Size, int* p3, int p3Size, int* p4, int p4Size){
    return is_square(p1,p2,p3,p4) || is_square(p1,p3,p4,p2) || is_square(p1,p2,p4,p3);
}


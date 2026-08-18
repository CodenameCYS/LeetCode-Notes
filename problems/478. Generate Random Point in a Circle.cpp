/*
=== 478. Generate Random Point in a Circle ===

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:
    1. input and output values are in floating-point.
    2. radius and x-y position of the center of the circle is passed into the class constructor.
    3. a point on the circumference of the circle is considered to be in the circle.
    4. randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:
    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[1,0,0],[],[],[]]
    Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:
    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[10,5,-7.5],[],[],[]]
    Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
    Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.
*/
// === 200ms(100%) && 32MB(100%) === //
typedef struct {
    double radius;
    double x0, y0;
} Solution;

Solution* solutionCreate(double radius, double x_center, double y_center) {
    srand((unsigned int)time(0));
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj -> radius = radius;
    obj -> x0 = x_center;
    obj -> y0 = y_center;
    return obj;
}

double* solutionRandPoint(Solution* obj, int* retSize) {
    double* p = (double*)malloc(2*sizeof(double));
    *retSize = 2;
    double theta = rand() / (1.0*RAND_MAX) * 2 * 3.1415926;
    double r = sqrt(rand() / (1.0*RAND_MAX)) * (obj -> radius);
    p[0] = obj->x0 + (r*cos(theta));
    p[1] = obj->y0 + (r*sin(theta));
    return p;
}

void solutionFree(Solution* obj) {
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(radius, x_center, y_center);
 * double* param_1 = solutionRandPoint(obj, retSize);
 
 * solutionFree(obj);
*/
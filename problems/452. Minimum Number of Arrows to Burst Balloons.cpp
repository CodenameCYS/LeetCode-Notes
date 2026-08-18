/*
=== 452. Minimum Number of Arrows to Burst Balloons ===

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:
    Input:
    [[10,16], [2,8], [1,6], [7,12]]
    Output:
    2
    Explanation:
    One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
*/
void quick_sort(int** points, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed;
    int* tmp = points[st];
    while(i<j){
        while(i<j && points[j][0] >= tmp[0]){
            -- j;
        }
        if(i < j){
            points[i] = points[j];
            ++ i;
        }
        while(i<j && points[i][0] <= tmp[0]){
            ++ i;
        }
        if(i<j){
            points[j] = points[i];
            -- j;
        }
    }
    points[i] = tmp;
    quick_sort(points, st, i-1);
    quick_sort(points, i+1, ed);
}

void show(int** points, int pointsSize){
    for(int i=0; i<pointsSize; ++i){
        printf("(%d,%d) ", points[i][0], points[i][1]);
    }
    printf("\n");
}
// === 352ms(25%) && 13MB(100%) === //
int findMinArrowShots(int** points, int pointsSize, int* pointsColSize){
    if(pointsSize <= 1){
        return pointsSize;
    }
    quick_sort(points, 0, pointsSize-1);
    // show(points, pointsSize);
    int ans = 0;
    int subset[2] = {points[0][0], points[0][1]};
    for(int i=1; i<pointsSize; ++i){
        subset[0] = points[i][0];
        subset[1] = subset[1] < points[i][1] ? subset[1] : points[i][1];
        if(subset[0] > subset[1]){
            ++ ans;
            subset[1] = points[i][1];
        }
    }
    return ans+1;
}


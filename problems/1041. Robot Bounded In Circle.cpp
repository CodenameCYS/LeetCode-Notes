/*
=== 1041. Robot Bounded In Circle ===

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
    - "G": go straight 1 unit;
    - "L": turn 90 degrees to the left;
    - "R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
    Input: "GGLLGG"
    Output: true
    - Explanation: 
    The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
    Input: "GG"
    Output: false
    - Explanation: 
    The robot moves north indefinetely.
Example 3:
    Input: "GL"
    Output: true
    - Explanation: 
    The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Note:
    1. 1 <= instructions.length <= 100
    2. instructions[i] is in {'G', 'L', 'R'}
*/
// === 4ms && 6.7MB === //
bool isRobotBounded(char * instructions){
    int x=0, y=0;
    int len = strlen(instructions);
    int direction = 0;
    for(int i=0; i<len; ++i){
        if(instructions[i] == 'G'){
            if(direction == 1){
                ++x;
            }
            else if(direction == 2){
                --y;
            }
            else if(direction == 3){
                --x;
            }
            else{
                ++y;
            }
        }
        else if(instructions[i] == 'R'){
            direction = ((direction + 1) % 4 + 4) % 4;
        }
        else{
            direction = ((direction - 1) % 4 + 4) % 4;
        }
    }
    if(direction == 0){
        return x == 0 && y == 0;
    }
    else{
        return true;
    }
}
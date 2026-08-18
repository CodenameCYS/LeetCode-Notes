/*
=== 874. Walking Robot Simulation ===

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:
-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units

Some of the grid squares are obstacles. 
The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)
Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:
1. 0 <= commands.length <= 10000
2. 0 <= obstacles.length <= 10000
3. -30000 <= obstacle[i][0] <= 30000
4. -30000 <= obstacle[i][1] <= 30000
5. The answer is guaranteed to be less than 2 ^ 31.

*/
# include <stdio.h>
# include <stdlib.h>

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesRowSize, int *obstaclesColSizes);

int main(){
    int commands[] = {4,-1,4,-2,4};
    int commandsSize = 5;
    int obstaclesRowSize = 1;
    int obstaclesColSizes = 2;
    int** obstacles = (int**)malloc(obstaclesRowSize * sizeof(int*));
    for(int i=0; i<obstaclesRowSize; ++i){
        obstacles[i] = (int*)malloc(2*sizeof(int));
    }
    obstacles[0][0] = 2,    obstacles[0][1] = 4;

    int ans = robotSim(commands, commandsSize, obstacles, obstaclesRowSize, &obstaclesColSizes);
    printf("%d\n",ans);

    system("pause");
    return 1;
}

/*
// === ver 1.0 --- array too large === //
int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesRowSize, int *obstaclesColSizes) {
    int obstaclerowlist[60001][10001];
    int obstaclecollist[60001][10001];
    for(int i=0; i<60001; ++i){
        obstaclerowlist[i][0] = 0;
        obstaclecollist[i][0] = 0;
    }
    for(int i=0; i<obstaclesRowSize; ++i){
        obstaclerowlist[obstacles[i][0]+30000][0] += 1;
        obstaclerowlist[obstacles[i][0]+30000][obstaclerowlist[obstacles[i][0]+30000][0]] = obstacles[i][1];

        obstaclecollist[obstacles[i][1]+30000][0] += 1;
        obstaclecollist[obstacles[i][1]+30000][obstaclerowlist[obstacles[i][1]+30000][0]] = obstacles[i][0];
    }

    int direction = 0; // 0 -> north    1 -> east  2 -> south   3 -> west
    int x = 0, y = 0;
    int distance = 0;
    for(int i=0; i<commandsSize; ++i){
        if(commands[i] == -1){
            direction = (direction + 1) % 4;
        }
        else if(commands[i] == -2){
            direction = (direction + 3) % 4;
        }
        else{
            int target;
            switch(direction){
                case 0:
                    target = y + commands[i];
                    for(int j=1; j<=obstaclerowlist[x+30000][0]; ++j){
                        if(y < obstaclerowlist[x+30000][j] && target >= obstaclerowlist[x+30000][j]){
                            target = obstaclerowlist[x+30000][j] - 1;
                        }
                    }
                    y = target;
                    break;
                case 1:
                    target = x + commands[i];
                    for(int j=1; j<=obstaclecollist[y+30000][0]; ++j){
                        if(x < obstaclecollist[y+30000][j] && target >= obstaclecollist[y+30000][j]){
                            target = obstaclecollist[y+30000][j] - 1;
                        }
                    }
                    x = target;
                    break;
                case 2:
                    target = y - commands[i];
                    for(int j=1; j<=obstaclerowlist[x+30000][0]; ++j){
                        if(y > obstaclerowlist[x+30000][j] && target <= obstaclerowlist[x+30000][j]){
                            target = obstaclerowlist[x+30000][j] + 1;
                        }
                    }
                    y = target;
                    break;
                case 3:
                    target = x - commands[i];
                    for(int j=1; j<=obstaclecollist[y+30000][0]; ++j){
                        if(x > obstaclecollist[y+30000][j] && target <= obstaclecollist[y+30000][j]){
                            target = obstaclecollist[y+30000][j] + 1;
                        }
                    }
                    x = target;
                    break;
            }
            distance = x*x + y*y > distance? x*x + y*y : distance;
        }
    }
    return distance;
}
*/

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesRowSize, int *obstaclesColSizes) {
    int direction = 0; // 0 -> north    1 -> east  2 -> south   3 -> west
    int x = 0, y = 0;
    int distance = 0;
    for(int i=0; i<commandsSize; ++i){
        if(commands[i] == -1){
            direction = (direction + 1) % 4;
        }
        else if(commands[i] == -2){
            direction = (direction + 3) % 4;
        }
        else{
            int target;
            switch(direction){
                case 0:
                    target = y + commands[i];
                    for(int j=0; j<obstaclesRowSize; ++j){
                        if(obstacles[j][0] == x && obstacles[j][1] > y && obstacles[j][1] <= target){
                            target = obstacles[j][1] - 1;
                        }
                    }
                    y = target;
                    break;
                case 1:
                    target = x + commands[i];
                    for(int j=0; j<obstaclesRowSize; ++j){
                        if(obstacles[j][1] == y && obstacles[j][0] > x && obstacles[j][0] <= target){
                            target = obstacles[j][0] - 1;
                        }
                    }
                    x = target;
                    break;
                case 2:
                    target = y - commands[i];
                    for(int j=0; j<obstaclesRowSize; ++j){
                        if(obstacles[j][0] == x && obstacles[j][1] < y && obstacles[j][1] >= target){
                            target = obstacles[j][1] + 1;
                        }
                    }
                    y = target;
                    break;
                case 3:
                    target = x - commands[i];
                    for(int j=0; j<obstaclesRowSize; ++j){
                        if(obstacles[j][1] == y && obstacles[j][0] < x && obstacles[j][0] >= target){
                            target = obstacles[j][0] + 1;
                        }
                    }
                    x = target;
                    break;
            }
            distance = x*x + y*y > distance? x*x + y*y : distance;
        }
    }
    return distance;
}

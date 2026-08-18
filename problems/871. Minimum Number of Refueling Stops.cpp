/*
=== 871. Minimum Number of Refueling Stops ===

A car travels from a starting position to a destination which is target miles east of the starting position.
Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.
The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.
When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.
Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 
Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Note:
1. 1 <= target, startFuel, stations[i][1] <= 10^9
2. 0 <= stations.length <= 500
3. 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
*/

# include <stdio.h>
# include <stdlib.h>
# include <iostream>
# include <vector>

using namespace std;
/*
=== 这部分代码有误，没考虑一个区间段内多次加油的情形 ===
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector< vector<int> >& stations) {

        int maxdistance = startFuel;
        if(maxdistance >= target){
            return 0;
        }

        int temp_station = 0;
        int count = 0;
        while(temp_station < stations.size()){
            if(stations[temp_station][0] > maxdistance){
                return -1;
            }
            else{
                int maxdistance_present = maxdistance;
                while(temp_station < stations.size() && stations[temp_station][0] <= maxdistance_present){
                    int temp_maxdistance = maxdistance_present + stations[temp_station][1];
                    maxdistance = maxdistance > temp_maxdistance ? maxdistance : temp_maxdistance;
                    ++ temp_station;
                }
                ++ count;

                if(maxdistance >= target){
                    return count;
                }
            }
        }

        return -1;
    }
};
*/

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector< vector<int> >& stations) {
        
        

        return -1;
    }
};

int main(){
    int target = 100;
    int startFuel = 10;

    vector< vector <int> > station(4 , vector<int>(2));

    station[0][0] = 10, station[0][1] = 60;
    station[1][0] = 20, station[1][1] = 30;
    station[2][0] = 30, station[2][1] = 30;
    station[3][0] = 60, station[3][1] = 40;

    for(int i = 0; i< station.size() ; ++i){
        printf("%d station's loc is %d, and has %d fuel!\n", i+1, station[i][0], station[i][1]);
    }

    class Solution s;
    int num = s.minRefuelStops(target, startFuel, station);
    
    if(num == -1){
        printf("\nCan't arrive destination.\n");
    }
    else{
        printf("\nAt least enter %d stations.\n", num);
    }
    system("pause");
}
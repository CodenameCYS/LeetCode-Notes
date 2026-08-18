/*
=== 841. Keys and Rooms ===

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). 
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Example 1:
    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:
    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.

Note:
    1. 1 <= rooms.length <= 1000
    2. 0 <= rooms[i].length <= 1000
    3. The number of keys in all rooms combined is at most 3000.
*/
// === 8ms(100%) && 6.1MB(100%) === //
bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize){
    int state[roomsSize];
    for(int i=0; i<roomsSize; ++i){
        state[i] = 0;
    }
    int stack[10001], size;
    stack[0] = 0, size = 1;
    while(size != 0){
        -- size;
        int room = stack[size];
        state[room] = 1;
        for(int j=0; j<roomsColSize[room]; ++j){
            if(state[rooms[room][j]] == 0){
                stack[size] = rooms[room][j];
                ++ size;
            }
        }
        // printf("room: %d -> %d\t", room, size);
    }
    for(int i=0; i<roomsSize; ++i){
        if(state[i] == 0){
            return false;
        }
    }
    return true;
}
'''
=== 2332. The Latest Time to Catch a Bus ===

You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.
You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.
The passengers will get on the next available bus. You can get on a bus that will depart at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.
Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.
Note: The arrays buses and passengers are not necessarily sorted.

Example 1:
    Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
    Output: 16
    Explanation: 
    The 1st bus departs with the 1st passenger. 
    The 2nd bus departs with you and the 2nd passenger.
    Note that you must not arrive at the same time as the passengers, which is why you must arrive before the 2nd passenger to catch the bus.
Example 2:
    Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
    Output: 20
    Explanation: 
    The 1st bus departs with the 4th passenger. 
    The 2nd bus departs with the 6th and 2nd passengers.
    The 3rd bus departs with the 1st passenger and you.
 
Constraints:
    1. n == buses.length
    2. m == passengers.length
    3. 1 <= n, m, capacity <= 105
    4. 2 <= buses[i], passengers[i] <= 109
    5. Each element in buses is unique.
    6. Each element in passengers is unique.
'''
# === 1541ms && 45.5MB === #
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        m, n = len(buses), len(passengers)
        buses = sorted(buses)
        passengers = sorted(passengers)
        record = [[] for _ in buses]
        idx = 0
        for i, t in enumerate(buses):
            while len(record[i]) < capacity and idx < n and passengers[idx] <= t:
                record[i].append(passengers[idx])
                idx += 1
            if len(record[i]) < capacity:
                record[i].append(t+1)
        # print(record)
        passengers = set(passengers)
        for i in range(m-1, -1, -1):
            for t in record[i][::-1]:
                if t-1 not in passengers:
                    return t-1
                
        return -1
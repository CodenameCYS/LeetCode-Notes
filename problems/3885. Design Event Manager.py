'''
=== 3885. Design Event Manager ===

You are given an initial list of events, where each event has a unique eventId and a priority.
Implement the EventManager class:
    - EventManager(int[][] events) Initializes the manager with the given events, where events[i] = [eventIdi, priority​​​​​​​i].
    - void updatePriority(int eventId, int newPriority) Updates the priority of the active event with id eventId to newPriority.
    - int pollHighest() Removes and returns the eventId of the active event with the highest priority. If multiple active events have the same priority, return the smallest eventId among them. If there are no active events, return -1.
An event is called active if it has not been removed by pollHighest().

Example 1:
    Input:
    ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]
    [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]
    Output:
    [null, 2, null, 5, 9]
    Explanation
    EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events
    eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2
    eventManager.updatePriority(9, 7); // event 9 now has priority 7
    eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5
    eventManager.pollHighest(); // return 9
Example 2:
    Input:
    ["EventManager", "pollHighest", "pollHighest", "pollHighest"]
    [[[[4, 1], [7, 2]]], [], [], []]
    Output:
    [null, 7, 4, -1]
    Explanation
    EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events
    eventManager.pollHighest(); // return 7
    eventManager.pollHighest(); // return 4
    eventManager.pollHighest(); // no events remain, return -1
 
Constraints:
    1. 1 <= events.length <= 105
    2. events[i] = [eventId, priority]
    3. 1 <= eventId <= 109
    4. 1 <= priority <= 109
    5. All the values of eventId in events are unique.
    6. 1 <= newPriority <= 109
    7. For every call to updatePriority, eventId refers to an active event.
    8. At most 105 calls in total will be made to updatePriority and pollHighest.
'''
# === 2145ms && 84.33MB === #
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.priority = defaultdict(int)
        self.q = []
        for event in events:
            self.addEvent(event)
        return

    def addEvent(self, event):
        id, priority = event
        if id in self.priority:
            self.updatePriority(id, priority)
        else:
            bisect.insort(self.q, (-priority, id))
            self.priority[id] = priority
        return

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        if eventId not in self.priority:
            return
        idx = bisect.bisect_left(self.q, (-self.priority[eventId], eventId))
        self.q.pop(idx)
        bisect.insort(self.q, (-newPriority, eventId))
        self.priority[eventId] = newPriority
        return

    def pollHighest(self) -> int:
        if self.q == []:
            return -1
        _, id = self.q.pop(0)
        self.priority.pop(id)
        return id


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
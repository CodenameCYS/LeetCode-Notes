'''
=== 855. Exam Room ===

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)
Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:
    Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
    Output: [null,0,9,4,2,null,5]
    Explanation:
    ExamRoom(10) -> null
    seat() -> 0, no one is in the room, then the student sits at seat number 0.
    seat() -> 9, the student sits at the last seat number 9.
    seat() -> 4, the student sits at the last seat number 4.
    seat() -> 2, the student sits at the last seat number 2.
    leave(4) -> null
    seat() -> 5, the student sits at the last seat number 5.
​​​​​​​
Note:
    1. 1 <= N <= 10^9
    2. ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
    3. Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
'''
# === 716ms(6.08%) && 14MB(79.33%) === #
class ExamRoom:

    def __init__(self, N: int):
        self.seat_num = N
        self.taken_seats = []

    def seat(self) -> int:
        if self.taken_seats == []:
            self.taken_seats.append(0)
            # print(self.taken_seats)
            return 0
        delta = 0
        idx = 0
        for i in range(1, len(self.taken_seats)):
            seat = (self.taken_seats[i] + self.taken_seats[i-1]) // 2
            if seat - self.taken_seats[i-1] > delta:
                delta = seat - self.taken_seats[i-1]
                idx = i
        seat = (self.taken_seats[idx] + self.taken_seats[idx-1]) // 2
        if self.taken_seats[0] != 0 and self.taken_seats[0]-0>=delta:
            seat = 0
            idx = 0
            delta = self.taken_seats[0] - 0
        if self.taken_seats[-1] != self.seat_num-1 and self.seat_num-1-self.taken_seats[-1] > delta:
            seat = self.seat_num-1
            idx = len(self.taken_seats)
            delta = self.seat_num-1-self.taken_seats[-1]
            
        self.taken_seats.insert(idx, seat)
        # print(self.taken_seats)
        return seat

    def leave(self, p: int) -> None:
        def search(st, ed):
            if ed - st <= 1:
                if self.taken_seats[st] == p:
                    return st
                else:
                    return ed
            mid = (st + ed) // 2
            if self.taken_seats[mid] == p:
                return mid
            elif self.taken_seats[mid] < p:
                st = mid+1
            else:
                ed = mid-1
            return search(st, ed)
        
        idx = search(0, len(self.taken_seats)-1)
        self.taken_seats.pop(idx)
        # print(self.taken_seats)
        return
                


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
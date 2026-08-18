'''
=== 2512. Reward Top K Students ===

You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.
Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.
You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.
Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

Example 1:
    Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
    Output: [1,2]
    Explanation: 
    Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
Example 2:
    Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
    Output: [2,1]
    Explanation: 
    - The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
    - The student with ID 2 has 1 positive feedback, so he has 3 points. 
    Since student 2 has more points, [2,1] is returned.
    
Constraints:
    1. 1 <= positive_feedback.length, negative_feedback.length <= 104
    2. 1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
    3. Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters.
    4. No word is present in both positive_feedback and negative_feedback.
    5. n == report.length == student_id.length
    6. 1 <= n <= 104
    7. report[i] consists of lowercase English letters and spaces ' '.
    8. There is a single space between consecutive words of report[i].
    9. 1 <= report[i].length <= 100
    10. 1 <= student_id[i] <= 109
    11. All the values of student_id[i] are unique.
    12. 1 <= k <= n
'''
# === 358ms && 22.7MB ===
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)
        n = len(student_id)
        
        def get_score(report):
            score = 0
            for w in report.split():
                if w in positive_feedback:
                    score += 3
                elif w in negative_feedback:
                    score -= 1
            return score
        
        score = [(get_score(report[i]), -student_id[i]) for i in range(n)]
        # print(score)
        score = sorted(score, reverse=True)[:k]
        return [-x[1] for x in score]
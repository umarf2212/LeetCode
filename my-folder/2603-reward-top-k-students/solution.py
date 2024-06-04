from collections import defaultdict
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        

        scores = defaultdict(int)

        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        n = len(report)
        for i in range(n):
            curStudentId = student_id[i]
            curScore = 0
            for word in report[i].split(' '):
                if word in positive_set:
                    curScore += 3
                
                elif word in negative_set:
                    curScore -= 1
            
            scores[curStudentId] = curScore
        
        print(scores)
        
        res = sorted(scores.items(), key=lambda x:(x[1], -x[0]), reverse=True)
        print(res)
        return [num[0] for num in res][:k]


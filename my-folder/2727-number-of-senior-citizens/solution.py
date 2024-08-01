class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        getPassengerAge = lambda detail: int(detail[11:13])

        count = 0
        for detail in details:
            if getPassengerAge(detail) > 60:
                count+=1
        
        return count

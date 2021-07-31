class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        # [type, color, name]
        # [phone, silver, pixel]
        
        count = 0
        index = {'type': 0, 'color': 1, 'name': 2}
        for item in items:
            
            if ruleKey=="type" and item[0] == ruleValue:
                count += 1
            elif ruleKey=="color" and item[1] == ruleValue:
                count += 1
            elif ruleKey=="name" and item[2] == ruleValue:
                count += 1
        
        return count
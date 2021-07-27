class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 0,2,4,5,6,9,10,12,13,15,17,20
        # 9, 4 -> 13 target
                
        low = 0
        high = len(numbers)-1
        
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low+1, high+1]
            
            elif numbers[low] + numbers[high] > target:
                high -= 1
            
            elif numbers[low] + numbers[high] < target:
                low += 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if target - numbers[i] in d:
                ar = [i+1, d[target-numbers[i]]+1]
                return [min(ar), max(ar)]
            else:
                d[numbers[i]] = i

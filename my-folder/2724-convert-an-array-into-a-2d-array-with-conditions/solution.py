class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        rows = [set()]
        for num in nums:

            for row in rows:
                if num not in row:
                    row.add(num)
                    break
            else:
                rows.append(set([num]))
            
        return [list(row) for row in rows]

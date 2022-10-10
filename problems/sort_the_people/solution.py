class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        ar = [[names[i], heights[i]] for i in range(len(names))]

        ar.sort(key=lambda x:x[1], reverse=True)

        return [name[0] for name in ar]
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if arr[-1] < x:
            return arr[-k:]
        
        if arr[0] > x:
            return arr[:k]

        def find_pos(arr, x):
            lo = 0
            hi = len(arr)-1
            mid = 0
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] >= x:
                    hi = mid
                else:
                    lo = mid+1
            return lo

        pos = find_pos(arr, x)
        # print(pos)
        i = pos-1
        j = pos
        res = []
        while len(res) < k:
            leftDiff = abs(arr[i]-x) if i >=0 else float('inf')
            rightDiff = abs(arr[j]-x) if j < len(arr) else float('inf')

            if leftDiff <= rightDiff:
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j+=1

        res.sort()
        return res



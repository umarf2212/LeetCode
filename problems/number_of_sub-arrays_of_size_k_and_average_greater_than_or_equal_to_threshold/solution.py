class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        ans = 0

        Sum = sum(arr[:k])

        if Sum//k >= threshold:
            ans += 1
        
        # 0 1 2 3 4 5 6 7 8
        # k = 3

        for j in range(k, len(arr)):
            i = j-k

            Sum += arr[j]
            Sum -= arr[i]

            if Sum//k >= threshold:
                ans += 1
        
        return ans

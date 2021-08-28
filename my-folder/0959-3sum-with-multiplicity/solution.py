class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        # 1 1 2 2 3 3 4 4 5 5
        #   i j             k
        
        # 1 + 2 2 2 --x-- 5 5
        # 6 -> 2's and 5's combinations
        
        arr.sort()
        count = 0
        
        for i in range(len(arr)):
            
            j = i+1
            k = len(arr) - 1
            
            while j < k:
                
                Sum = arr[i] + arr[j] + arr[k]
                
                
                if Sum == target:
                    if arr[j] == arr[k]:
                        sameCount = k-j+1
                        count += sameCount*(sameCount-1)//2
                        break
                    else:
                        j_count = 1
                        while j < k and arr[j] == arr[j+1]:
                            j_count += 1
                            j+=1
                        
                        k_count = 1
                        while j < k and arr[k] == arr[k-1]:
                            k_count += 1
                            k-=1

                        count += j_count * k_count
                        
                        j+=1
                        k-=1
                elif Sum < target:
                    j += 1
                else:
                    k -= 1
                
        return count % 1000000007

# 3 8 0 9 2 5

# ind = 0
# arr[ind+1]

# [3, 8, 1, 2, 0, 5, 5, 9]

# [3, 8, 1, 5, 5, 9]

# n=2
# [1, 8, 1, 5, 5, 9]
# => 8

# [1, 8, 1, 5, 5, 9]
# n=2
# 

# n > arr[ind]
# while n >= arr[ind]
#   n = n - arr[ind]
#   arr[ind] = 0
#   ind += 2

# if n == 0:
# return arr[ind-1]

# n <= arr[ind]
#   arr[ind] = arr[ind] - n
#   return arr[ind+1]


class RLEIterator:

    def __init__(self, encoding: List[int]):
        # copy the array
        self.encoding = encoding[:] # O(n)

        # iterator
        self.itr = 0

    def next(self, n: int) -> int:

        while self.itr < len(self.encoding):

            if n <= self.encoding[self.itr]:
                self.encoding[self.itr] -= n
                return self.encoding[self.itr+1]
            
            # freq = 0 is also handled here itself
            # if self.encoding[self.itr] == 0
            # since n >= 1; below line will be n -= 0
            n -= self.encoding[self.itr]
            self.itr += 2
        
        return -1


        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

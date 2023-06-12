class Solution:
    def customSortString(self, order: str, s: str) -> str:

        order = {order[i]:i for i in range(len(order))}

        ar = []
        ar2 = []
        for c in s:
            if c in order:
                ar.append(c)
            else:
                ar2.append(c)

        # quick sort
        def quickSort(ar):
            if len(ar) <= 1:
                return ar
            pivot = ar[0]
            greater = [x for x in ar[1:] if order[x]-order[pivot] >= 0]
            smaller = [x for x in ar[1:] if order[x]-order[pivot] < 0]
            return quickSort(smaller) + [pivot] + quickSort(greater)
 
        ar = quickSort(ar) + ar2

        return ''.join(ar)

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        orders.sort(key=lambda x: x[2], reverse=True)
        
        d = {}
        foods = {}
        
        for order in orders:
            if order[1] in d:
                d[order[1]].append(order[2])
            else:
                d[order[1]] = [order[2]]
            
            # needs Opt
            foods[order[2]] = 1
        
        # needs Opt
        foodItems = list(foods.keys())[::-1]
        header = ["Table"] + foodItems
        
        res = [header]
        for table in sorted(d.keys(), key=lambda x: int(x)):
            currentTable = [table] + ["0" for _ in range(len(foodItems))]
            
            while d[table]:
                currentFood = d[table].pop()
                count = 1
                while d[table] and d[table][-1] == currentFood:
                    d[table].pop()
                    count+=1
                
                # needs Opt
                i=1
                while i<len(foodItems) and foodItems[i-1] != currentFood:
                    i+=1
                
                currentTable[i] = str(count)
            
            res.append(currentTable)
        
        return res
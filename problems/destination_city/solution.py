class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        allCities = set()
        
        for cities in paths:
            allCities.add(cities[0])
        
        for cities in paths:
            if cities[1] not in allCities:
                return cities[1]
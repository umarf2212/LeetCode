class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        newTitle = ''
        for word in title.split():
            
            if len(word) <= 2:
                newTitle += word.lower() + ' '
            else:
                newTitle += word.capitalize() + ' '
        
        return newTitle[:len(newTitle)-1]

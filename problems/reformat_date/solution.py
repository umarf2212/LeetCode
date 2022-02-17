class Solution:
    def reformatDate(self, date: str) -> str:
        
        
        date = date.split(' ')
        
        months = {
            "Jan":'01', 
            "Feb":'02', 
            "Mar":'03', 
            "Apr":'04', 
            "May":'05', 
            "Jun":'06', 
            "Jul":'07', 
            "Aug":'08', 
            "Sep":'09', 
            "Oct":'10', 
            "Nov":'11', 
            "Dec":'12'
        }
        
        y = date[2]
        m = months[date[1]]
        d = date[0][:len(date[0])-2]
        
        if len(d) == 1:
            d = '0'+d
        
        return y + '-' + m + '-' + d
class Logger:

    def __init__(self):
        self.logger = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        # If message is new, add it to logger and return True
        if message not in self.logger:
            self.logger[message] = timestamp
            return True
        
        # If message is duplicate, check if prev message was 
        # added withing 10 seconds. If it did, then we simply return False
        # otherwise, since more than 10 seconds have elpased, we print
        # current message and update its entry as well.
        if timestamp - self.logger[message] >= 10:
            self.logger[message] = timestamp
            return True
        else:
            return False
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

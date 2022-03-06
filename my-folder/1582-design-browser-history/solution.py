class BrowserHistory:
    
    ## Doubly Linked List
    class History:
        def __init__(self, homepage):
            self.page = homepage
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):
        self.homepage = self.History(homepage)
        self.currentPage = self.homepage
        
    def visit(self, url: str) -> None:
        newPage = self.History(url)
        self.currentPage.next = newPage
        newPage.prev = self.currentPage
        self.currentPage = newPage
        
        return self.currentPage.page
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.currentPage != self.homepage:
            self.currentPage = self.currentPage.prev
            steps -= 1
        
        return self.currentPage.page

    def forward(self, steps: int) -> str:
        while steps > 0 and self.currentPage.next:
            self.currentPage = self.currentPage.next
            steps -= 1
            
        return self.currentPage.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

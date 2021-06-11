class Solution:
    def makeEmail(self, s):
        localName = s.split('+')
        if len(localName) == 1:
            localName = s.split('@')[0]
        else:
            localName = localName[0]
        localName = ''.join(localName.split('.'))
        domainName = s.split('@')[1]
        return localName+'@'+domainName
        
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        
        for email in emails:
            email = self.makeEmail(email)
            
            if email not in d:
                d[email] = 1
        print(d)
        return len(d.values())
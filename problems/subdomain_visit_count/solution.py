class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        d = {}
        for cpd in cpdomains:
            count, domain = cpd.split(" ")
            count = int(count)
            
            doms = []
            domain = domain.split(".")
            for i in range(len(domain)-1,-1,-1):
                doms.append('.'.join(domain[i:]))
            
            for dom in doms:
                if dom in d:
                    d[dom] += count
                else:
                    d[dom] = count
        
        res = []
        for dom, count in d.items():
            res.append(str(count)+" "+dom)
        
        return res
                    
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:

        regex = r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"
        matcher = re.findall(regex, formula)

        print(matcher)

        stack = [defaultdict(int)]

        for atom, count, left, right, multiplier in matcher:
            if atom:
                stack[-1][atom] += int(count) if count else 1
            
            elif left:
                stack.append(defaultdict(int))

            elif right:
                curr_map = stack.pop()
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier
                
                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]
        
        final_map = dict(sorted(stack[0].items()))

        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        
        return ans
                        




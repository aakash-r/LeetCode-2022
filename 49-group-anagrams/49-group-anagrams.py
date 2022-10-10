class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            l = ''.join(sorted(i))
            d[l].append(i)
        
        return d.values()
            
                
            
            
        
            
        
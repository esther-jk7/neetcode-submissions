class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            key = "".join(sorted(word))
            
            if key in results:
                results[key].append(word)
            else:
                results[key] = [word]
        
        return list(results.values())
        
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for ch in word:
                char_count[ord(ch)- ord('a')] += 1
            
            results[tuple(char_count)].append(word)

        return results.values()
        

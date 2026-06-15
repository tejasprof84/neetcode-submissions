class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a dictionary where the default value for a new key is an empty list
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the characters of the word to create a unique signature
            # e.g., "eat" -> ['a', 'e', 't'] -> "aet"
            sorted_key = "".join(sorted(word))
            
            # Append the original word to its matching anagram group
            anagram_map[sorted_key].append(word)
            
        # Return all the grouped sublists
        return list(anagram_map.values())

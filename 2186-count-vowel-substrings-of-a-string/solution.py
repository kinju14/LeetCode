class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total_count = 0
        n = len(word)
        
        # Helper function to count valid substrings in a vowel-only segment
        def countValidSubstrings(s: str):
            left = 0
            vowel_count = {}
            count = 0
            
            for right in range(len(s)):
                char = s[right]
                vowel_count[char] = vowel_count.get(char, 0) + 1
                
                # Ensure the window contains all five vowels
                while len(vowel_count) == 5:
                    count += len(s) - right  # All substrings starting from `left` to `right`
                    vowel_count[s[left]] -= 1
                    if vowel_count[s[left]] == 0:
                        del vowel_count[s[left]]
                    left += 1
            
            return count

        i = 0
        while i < n:
            if word[i] in vowels:
                start = i
                while i < n and word[i] in vowels:
                    i += 1
                total_count += countValidSubstrings(word[start:i])  # Process the vowel-only segment
            i += 1

        return total_count


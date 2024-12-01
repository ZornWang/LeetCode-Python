class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        if len(ransomNote) > len(magazine):
            return False
        for i in magazine:
            record[ord(i) - ord("a")] += 1
        for i in ransomNote:
            record[ord(i) - ord("a")] -= 1
            if record[ord(i) - ord("a")] < 0:
                return False
        return True

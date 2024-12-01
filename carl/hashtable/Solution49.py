from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for str in strs:
            record = [0] * 26
            for ch in str:
                record[ord(ch) - ord("a")] += 1
            mp[tuple(record)].append(str)

        return list(mp.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))

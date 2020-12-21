"""
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:

Input: "leetcode"
Output: "tcode"

 

Note:

    1 <= s.length <= 4 * 10^5
    s contains only lowercase English letters.


"""
class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(ans, s[i:])
        return ans  
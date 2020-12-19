"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""

 

Constraints:

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = []
        if str1 + str2 != str2 + str1:
            answer.append("")
        else:
            number_of_strings = min(len(str1), len(str2))
            for i in range(number_of_strings, 0, -1):
                #check for gcd
                if (len(str1) % i == 0 and len(str2) % i == 0 ):
                    string = str1[:i]
                    #check for division
                    m1 = int(len(str1)/i)
                    m2 = int(len(str2)/i)
                    if(string*m1 == str1 and string*m2 == str2):
                        answer.append(string)
        return answer[0]        
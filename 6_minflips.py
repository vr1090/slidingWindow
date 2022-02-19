"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        double = s + s
        count1 = 0
        count2 = 0
        result = n
        pt1 =""
        pt2=""
        
        for i in range(len(double)):
            pt1 += "0" if i %2 ==0 else "1"
            pt2 += "1"if i %2 ==0 else "0"
        
        
        l = 0
        
        for r in range(len(double)):
            
            if double[r]!=pt1[r]:
                count1 += 1
            
            if double[r] != pt2[r]:
                count2 += 1
                
            if (r-l+1) > n :
                if double[l] != pt1[l]:
                    count1 -=1
                if double[l] != pt2[l]:
                    count2 -=1
                
                l = l + 1
            
            if (r-l+1) == n:
                result = min(result, count1, count2)
            
        
        return result
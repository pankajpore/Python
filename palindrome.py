
def checkPolindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True 
    
def longestPalindromeBruteForce(s):
    if len(s) == 1:
        return s

    output = ""
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            flag = checkPolindrome(s, i, j)
            if flag and len(output) <  j - i + 1:
                    output = s[i: j + 1]
    return output 


def longestPalindromeExpansionFromCenter(s):
    if len(s) == 1 or len(s) == 0:
        return s
    
    start, maxLen = 0, 1
    for i in range (0, len(s)):
        for j in range(0, 2):
            low, high = i, i + j
            
            while low > 0 and high < len(s) and s[low] == s[high]:
                currLen = high - low + 1
                if currLen > maxLen:
                    start = low
                    maxLen = currLen 
                low -=  1
                high += 1
    return s[start :  start + maxLen]            

"""

abababa


"""
def longestPalindromeManacher(s):
    return ""
    
    


if __name__ == "__main__":
    s = "forgeeksskeegfor"
    
    print("longestPalindromeBruteForce: %s, Len: %d" % (longestPalindromeBruteForce(s), len(longestPalindromeBruteForce(s))))
    print("longestPalindromeExpansionFromCenter: %s, Len: %d" % (longestPalindromeExpansionFromCenter(s), len(longestPalindromeExpansionFromCenter(s))))
    print("longestPalindromeManacher: %s, Len: %d" % (longestPalindromeManacher(s), len(longestPalindromeManacher(s))))
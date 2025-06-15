MAX_CHAR = 26

def longestUniqueSubstr_Pointer(s):
    '''
        Input: aebcdefghijklmn
         Parsing: 
            a 
            a e 
            a e b 
            a e b c 
            a e b c d 
            a e b c d e => 5 =>  
            b c d e f 
            b c d e f g ......        
    '''

    if len(s) < 2:
        return len(s)
    
    left, right, res = 0, 0, 0
    visited = [False] * 26
    
    while right < len(s):
        
        while visited[ord(s[right]) - ord('a')] == True:
            visited[ord(s[left]) - ord('a')] = False
            left += 1
            
        
        visited[ord(s[right]) - ord('a')] = True
        res =  max(res, right - left + 1)
        right += 1
    
    return res    

if __name__ == "__main__":
    s = "aebcdefghijklmn"
    print(longestUniqueSubstr_Pointer(s))

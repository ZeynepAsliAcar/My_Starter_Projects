def palindrome(S):
    OPT = new int[S.length][S.length + 1]
 
    for i = 0 to S.length - 1:
        for n = 0 to 1:
            OPT[i][n] = n
    
    for n = 2 to S.length:
        for i = 0 to S.length - n:
            if S[i] == S[i + n - 1]  and  OPT[i+1][n-2] == n-2:
                OPT[i][n] = 2 + OPT[i+1][n-2]
            else:
                OPT[i][n] = max(OPT[i][n-1], OPT[i+1][n-1])
    
    return OPT[0][S.length]

def longest_palindrome_subseq(S):
    n = len(S)
    OPT = [[0] * n for _ in range(n)]

    for i in range(n):
        OPT[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                if length == 2:
                    OPT[i][j] = 2
                else:
                    OPT[i][j] = 2 + OPT[i + 1][j - 1]
            else:
                OPT[i][j] = max(OPT[i + 1][j], OPT[i][j - 1])

    return OPT[0][n - 1]

S = input("Bir string girin: ")
print("En uzun palindromik alt dizinin uzunluğu:", longest_palindrome_subseq(S))

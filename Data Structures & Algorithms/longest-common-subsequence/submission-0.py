class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        visited = {}
        
        def LCS(i, j):
            if i < len(text1) and j < len(text2):
                if (i, j) not in visited:
                    if text1[i] == text2[j]:
                        localLCS = 1 + LCS(i + 1, j + 1)
                        visited[(i, j)] = localLCS
                        return localLCS
                    else:
                        shift1 = LCS(i + 1, j)
                        shift2 = LCS(i, j + 1)
                        localLCS = max(shift1, shift2)
                        visited[(i, j)] = localLCS
                        return localLCS
                else:
                    return visited[(i, j)]
            else:
                return 0
        
        return LCS(0, 0)
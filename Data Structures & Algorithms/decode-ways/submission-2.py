class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(idx):

            if idx in memo:
                return memo[idx]

            if idx == len(s) - 1:
                if int(s[idx]) == 0:
                    return 0
                return 1
            elif idx >= len(s) - 1:
                return 1

            if int(s[idx]) > 2:
                if int(s[idx + 1]) == 0:
                    memo[idx] = 0
                    return 0
                else:
                    single = decode(idx + 1)
                    memo[idx] = single
                    return single

            elif int(s[idx]) == 2:
                if int(s[idx + 1]) == 0:
                    double = decode(idx + 2)
                    memo[idx] = double
                    return double
                elif int(s[idx + 1]) > 6:
                    single = decode(idx + 1)
                    memo[idx] = single
                    return single
                else:
                    single = decode(idx + 1)
                    double = decode(idx + 2)
                    if single == 0 and double == 0:
                        memo[idx] = 0
                        return 0
                    else:
                        memo[idx] = single + double
                        return single + double

            elif int(s[idx]) == 1:
                if int(s[idx + 1]) == 0:
                    single = decode(idx + 2)
                    memo[idx] = single
                    return single
                else:
                    single = decode(idx + 1)
                    double = decode(idx + 2)
                    if single == 0 and double == 0:
                        memo[idx] = 0
                        return 0
                    else:
                        memo[idx] = single + double
                        return single + double

            else:
                memo[idx] = 0
                return 0

        return decode(0)
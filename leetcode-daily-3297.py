def validSubstringCount(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d2 = {}
        dd2 = []
        r = []
        for i in word2:
            if d2.get(i) is None:
                d2[i] = 1
            else:
                d2[i] += 1
        for i in range(len(word1)):
            dd2.append(d2.copy())
            if d2.get(word1[i]) is not None:
                for j in range(len(dd2) - 1, -1, -1):
                    if dd2[j][word1[i]] > 0:
                        dd2[j][word1[i]] -= 1
                    if sum(dd2[j].values()) == 0:
                        del dd2[j]
                        r.append(i)
        r = [len(word1) - n for n in r]
        return sum(r)

print(validSubstringCount("dcbdcdccb", "cdd"))
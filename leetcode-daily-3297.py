def validSubstringCount(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d2 = {}
        s = []
        dd2 = []
        for i in word2:
            if d2.get(i) is None:
                d2[i] = 1
            else:
                d2[i] += 1
        for i in range(len(word1)):
            s.append(0)
            dd2.append(d2.copy())
            if d2.get(word1[i]) is not None:
                for j in dd2:
                    if j[word1[i]] > 0:
                        j[word1[i]] -= 1
            for j in range(len(dd2)):
                if sum(dd2[j].values()) == 0:
                    s[j] += len(word1) - i
                    dd2[j]['1'] = -1
            
        return sum(s)

print(validSubstringCount("dcbdcdccb", "cdd"))
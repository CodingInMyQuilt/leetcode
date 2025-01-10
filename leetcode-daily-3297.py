def validSubstringCount(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d2 = {}
        s = 0
        for i in word2:
            if d2.get(i) is None:
                d2[i] = 1
            else:
                d2[i] += 1
        for i in range(len(word1)):
            d22 = d2.copy()
            w3 = word1[i:]
            if len(w3) < len(word2):
                break
            else:
                for j in range(len(w3)):
                    if d2.get(w3[j]) is None:
                        continue
                    else:
                        if d22.get(w3[j]) > 0:
                            d22[w3[j]] -= 1
                    if sum(d22.values()) == 0:
                        s += len(w3) - j
                        break
        return s
def validSubstringCount(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d2 = {}
        r = []
        a = 0
        for i in word2:
            if d2.get(i) is None:
                d2[i] = 1
            else:
                d2[i] += 1
        for i in range(len(word1)):
            if d2.get(word1[i]) is not None:
                d2[word1[i]] -= 1
                x = 1
                for j in d2.values():
                    if j > 0:
                        x = 0
                        break
                if x == 1:
                    while x == 1:
                        if d2.get(word1[a]) is not None:
                            d2[word1[a]] += 1
                        a += 1
                        r.append(i)
                        for j in d2.values():
                            if j > 0:
                                x = 0
                                break
        r = [len(word1) - n for n in r]
        return sum(r)

print(validSubstringCount("bcca", "abc"))

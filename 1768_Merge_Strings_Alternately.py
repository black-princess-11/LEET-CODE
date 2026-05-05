class Solution(object):
    def mergeAlternately(self, word1, word2):
        w1=list(word1.lower())
        w2=list(word2.lower())
        mergeWord=[""]
        if len(w1) > len(w2):
            for i in range(0,len(w1)):
                if i < len(w1):
                    mergeWord.append(w1[i])
                if i < len(w2):
                    mergeWord.append(w2[i])
        elif len(w1) < len(w2):
            for i in range(0,len(w2)):
                if i < len(w1):
                    mergeWord.append(w1[i])
                if i < len(w2):
                    mergeWord.append(w2[i])
        else:
            for i in range(0,len(w1)):
                mergeWord.append(w1[i])
                mergeWord.append(w2[i])
        newWord=str("".join(mergeWord))
        return newWord
print(Solution().mergeAlternately(word1="abc",word2="pqr"))
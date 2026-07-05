class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            print(False)
        count1={}
        count2={}
        for letter in s:
            count1[letter]=count1.get(letter,0)+1
        for letter1 in t:
            count2[letter1]=count2.get(letter1,0)+1
        if count1==count2:
            return True
        else:
            return False
        
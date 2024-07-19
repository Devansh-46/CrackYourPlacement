class Solution:
    def Anagrams(self, words, n):
        ret_val = []
        while(len(words) > 0):
            group_list = []
            
            word_i = words[0]
            group_list.append(word_i)

            anagram_words = [a for a in words[1::] if self.isAnagram(word_i, a)]
            group_list.extend(anagram_words)

            ret_val.append(group_list)
            words = [a for a in words[1::] if not self.isAnagram(word_i, a)]

        return ret_val

    def isAnagram(self, str_1, str_2):
        a_dict = {}
        for i in range(0, len(str_1)):
            chr_1 = str_1[i:i+1]
            if (chr_1 not in a_dict):
                a_dict[chr_1] = 0
            a_dict[chr_1] += 1
        
        b_dict = {}
        for i in range(0, len(str_2)):
            chr_2 = str_2[i:i+1]
            if (chr_2 not in b_dict):
                b_dict[chr_2] = 0
            b_dict[chr_2] += 1

        return a_dict == b_dict

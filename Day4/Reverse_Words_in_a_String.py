class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        ans = ""
        for i in s_list[::-1]:
            if i == "":
                continue
            else:
                ans = ans + " " + i

        return ans.strip()
        
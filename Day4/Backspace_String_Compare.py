class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        stack1 = list()
        stack2 = list()

        for i in s_list:
            if len(stack1) > 0 and i =='#':
                stack1.pop()
            elif len(stack1) == 0 and i =='#':
                continue
            else:
                stack1.append(i)

        for j in t_list:
            if len(stack2) > 0 and j =='#':
                stack2.pop()
            elif len(stack2) == 0 and j =='#':
                continue
            else:
                stack2.append(j)
        
        if stack1 == stack2:
            return True
        return False

        
        
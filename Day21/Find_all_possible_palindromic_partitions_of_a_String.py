# A utility function to check if 
# str is palindrome
def isPalindrome(string: str,
                 low: int, high: int):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


# Recursive function to find all 
# palindromic partitions of str[start..n-1]
# allPart --> A vector of vector of strings. 
#             Every vector inside it stores a partition
# currPart --> A vector of strings to store current partition
def allPalPartUtil(allPart: list, currPart: list, 
                   start: int, n: int, string: str):

    # If 'start' has reached len
    if start >= n:
        
        # In Python list are passed by reference
        # that is why it is needed to copy first
        # and then append
        x = currPart.copy()

        allPart.append(x)
        return

    # Pick all possible ending points for substrings
    for i in range(start, n):

        # If substring str[start..i] is palindrome
        if isPalindrome(string, start, i):

            # Add the substring to result
            currPart.append(string[start:i + 1])

            # Recur for remaining remaining substring
            allPalPartUtil(allPart, currPart, 
                            i + 1, n, string)

            # Remove substring str[start..i] 
            # from current partition
            currPart.pop()

class Solution:
    def allPalindromicPerms(self, S):
        # code here
        n = len(S)

        # To Store all palindromic partitions
        allPart = []

        # To store current palindromic partition
        currPart = []

        # Call recursive function to generate 
        # all partitions and store in allPart
        allPalPartUtil(allPart, currPart, 0, n, S)
        
        return allPart

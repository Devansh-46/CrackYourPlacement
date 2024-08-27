class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        level = self.root
        for c in word:
            if not (c in level): 
                level[c] = {}
            level = level[c]
        level['end'] = True

    def search(self, word: str) -> bool:
        return dfs(self.root, word)

def dfs(root, s):
    # if it the end of the word return we found it
    if len(s) == 0 and ('end' in root): return True
    # if is the end of the word but not marked as end we return false
    if len(s) == 0: return False
    # if it is a . we shoud traverse all nodes and try to find a match
    if s[0] == '.':
        for c in root:
            if c != 'end':
                # if we found one we return True
                if dfs(root[c], s[1:]): return True
    # if we don't find the letter in next level e return false
    if  (s[0] not in root): return False
    # search next level
    return dfs(root[s[0]], s[1:])       



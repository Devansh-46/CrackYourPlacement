#User function Template for python3

class trieNode:
    def __init__(self):
        self.child=[None]*(26) # initialize an array of 26 elements for child nodes
        self.isLast=False # flag to indicate if the current node is the last character of a contact
        
class Trie:
    def __init__(self):
        self.root=trieNode() # initialize the root node of the trie
        
    def insert(self,a):
        curr=self.root # start from the root node
        for el in a:
            if curr.child[ord(el)-ord("a")]==None: # if the child node does not exist
                curr.child[ord(el)-ord("a")]=trieNode() # create a new node for the character
            curr=curr.child[ord(el)-ord("a")] # move to the child node
        curr.isLast=True # mark the node as the last character of a contact
        
    def insertIntoTrie(self,contact,n):
        for i in range(n):
            self.insert(contact[i]) # insert each contact into the trie
            

class Solution:
    def displayContactsUtil(self,curNode,prefix,vec):
        if curNode.isLast: # if it is the last character of a contact
            vec.append(prefix) # add the contact to the vector
        for c in range(26):
            i=chr(ord("a")+c) # get the character (a-z)
            nextNode=curNode.child[c] # get the child node for the character
            if nextNode!=None:
                self.displayContactsUtil(nextNode,prefix+i,vec) # recursively call the function for the next character
        

    def displayContacts(self, n, contact, s):
        trie=Trie() # create a trie
        trie.insertIntoTrie(contact,n) # insert the contacts into the trie
        prevnode=trie.root # set the previous node as the root node
        res=[]
        prefix=""
        _len=len(s)
        i=0
        while i<_len:
            v=[]
            prefix+=s[i] # add the current character to the prefix
            last_char=prefix[i] # get the last character of the prefix
            curNode=prevnode.child[ord(last_char)-ord("a")] # get the child node for the last character
            if curNode is None: # if the child node does not exist, there are no matching contacts
                v.append("0")
                res.append("0")
                i+=1
                break
            else:
                self.displayContactsUtil(curNode,prefix,v) # find all contacts starting with the prefix
                prevnode=curNode # update the previous node
                res.append(v[:]) # add the matching contacts to the result
                i+=1
                
        while i<_len:
            res.append(["0"]) # if there are no more characters in the string, add "0" to the result
            i+=1
        return res # return the result as a list of lists containing matching contacts for each prefix

//User function Template for 

class TrieNode {
  constructor() {
    this.children = new Array(26).fill(null);
    this.isEndOfWord = false;
  }
}

class Solution {
  insert(root, key) {
    let node = root;
    for (let i = 0; i < key.length; i++) {
      let index = key.charCodeAt(i) - 'a'.charCodeAt(0);
      if (node.children[index] === null) {
        node.children[index] = new TrieNode();
      }
      node = node.children[index];
    }
    node.isEndOfWord = true;
  }

  search(root, key) {
    let node = root;
    for (let i = 0; i < key.length; i++) {
      let index = key.charCodeAt(i) - 'a'.charCodeAt(0);
      if (node.children[index] === null) {
        return false;
      }
      node = node.children[index];
    }
    return (node !== null && node.isEndOfWord);
  }

  wordBreakutil(str, root) {
    let size = str.length;
    if (size === 0) return true;
    for (let i = 1; i <= size; i++) {
      if (this.search(root, str.substring(0, i)) && this.wordBreakutil(str.substring(i, size), root)) {
        return true;
      }
    }
    return false;
  }

  wordBreak(A, B) {
    //code here
    let root = new TrieNode();
    for (let i = 0; i < B.length; i++) {
      this.insert(root, B[i]);
    }
    return this.wordBreakutil(A, root) ? 1 : 0;
  }
}

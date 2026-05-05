from collections import deque

class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode()
                node.children[letter] = new_node
                node = new_node

        node.end_of_word = True 
        

    def search(self, word: str) -> bool:
        node = self.root
        return self.searchHelper(word,node)
        
    def searchHelper(self,word:str,node:TrieNode) -> bool:
        for i,letter in enumerate(word):
            if not letter=='.':
                if letter in node.children:
                    node = node.children[letter]
                else:
                    return False
            else:
                found = False
                for possible_node in node.children.values():
                    found = found or self.searchHelper(word[i+1:],possible_node)
                return found


        else:
            return node.end_of_word
        

class PrefixNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = PrefixNode()
                node.children[letter] = new_node
                node = new_node
        node.end_of_word = True
                
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        else:
            return node.end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        

        return True

        
        
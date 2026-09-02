class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end_of_word
            
            if word[i] in node.children:
                if dfs(i + 1, node.children[word[i]]):
                    return True
            elif word[i] == ".":
                for child in node.children:
                    if dfs(i + 1, node.children[child]):
                        return True
            return False
        return dfs(0, self.root)
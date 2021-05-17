class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        "Inserting a word to trie."
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]
            node.counter += 1
        node.is_end = True

    def dfs(self, node, prefix):
        "Helper function for query. Depth First Search"
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        "Search a keyword in trie."
        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])
        return f"result: {node.counter}, {self.output}"

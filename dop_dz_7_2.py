class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:

        stack = [(self.root, word)]

        while stack:
            node, word = stack.pop()

            if not word:
                if node.isEnd:
                    return True

            elif word[0] in node.children:
                temp = node.children[word[0]]
                stack.append((temp, word[1:]))

            elif word[0] == '.':
                for temp in node.children.values():
                    stack.append((temp, word[1:]))

        return False

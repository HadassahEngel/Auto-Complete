

class Node:
    """Define a single node in the trie"""

    def __init__(self, char):
        self.char = char
        self.sentences_indexes = {}
        self.children = {}
        self.is_leaf = True


class SentencesTrie:

    def __init__(self):
        self.root = Node("")

    def insert_sentence(self, sentence, index):
        """Insert the sentence to the trie"""
        sentence = sentence.lower()
        current_node = self.root
        for ch in sentence:
            if index[0] not in current_node.sentences_indexes:
                current_node.sentences_indexes[index[0]] = index[1]
            if not current_node.is_leaf:
                if ch not in current_node.children:
                    current_node.children[ch] = Node(ch)
            else:
                current_node.is_leaf = False
                current_node.children[ch] = Node(ch)
            current_node = current_node.children[ch]
        current_node.sentences_indexes[index[0]] = index[1]

    def search_sentence(self, sentence, node):
        """Search for a sentence in the trie, start in the given node"""
        sentence = sentence
        current_node = self.root
        for ch in sentence:
            if ch not in current_node.children or current_node.is_leaf:
                return None, node
            current_node = current_node.children[ch]
        return current_node.sentences_indexes, current_node


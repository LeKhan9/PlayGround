from data_structures.node import TrieNode

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        '''
            Iteratively adds each character as a rooted node in the Trie

        :param word: str representation of a word
        '''

        curr_trie = self.root
        for i, char in enumerate(word):
            if char not in curr_trie:
                curr_trie.add_letter(char)

            # move on to the next letter and create another TrieNode
            curr_trie = curr_trie.get(char)

        curr_trie.mark_complete_word()


    def search(self, word):
        '''
            Search the tree paths one character at a time

        :param word: str representation of a word
        '''

        curr_trie = self.root
        for i, char in enumerate(word):
            if char not in curr_trie:
                return False

            curr_trie = curr_trie.get(char)

        # word is found if this path ends here at a marked word
        return curr_trie.is_complete_word()


    def starts_with(self, prefix):
        '''
            Similar to the search function, but searches only for a prefix and not just
            sentinal marked words

        :param word: str representation of a prefix of a word
        '''

        curr_trie = self.root
        for i, char in enumerate(prefix):
            if char not in curr_trie:
                return False

            curr_trie = curr_trie.get(char)

        return True

    def __repr__(self):
        return f'[{self.root}]'

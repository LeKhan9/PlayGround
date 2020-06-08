from data_structures.trie import Trie

def generate_sample_trie_with_word_list(word_ls=['abe', 'cat']):
    trie = Trie()

    for word in word_ls:
        trie.insert(word)

    '''
        [[] -> [{'a': [a] -> [{'b': [b] -> [{'e': [e] -> [{}] ***}] }] ,
             'c': [c] -> [{'a': [a] -> [{'t': [t] -> [{}] ***}] }] }] ]
    '''

    return trie

##costruction of Trie for quickly finding suffixes


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char]=TrieNode()

    def find_suffix(self, node):
        out=[]
        for i in node.children:
            if node.children[i].is_word:
                out+=[i]
            out+= [i+a for a in self.find_suffix(node.children[i])]
        return out

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        cur_node=self
        for c in suffix:
            if c in cur_node.children:
                cur_node= cur_node.children[c]
        return self.find_suffix(cur_node)

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur_node=self.root
        for cha in word:
            cur_node.insert(cha)
            cur_node=cur_node.children[cha]
        cur_node.is_word=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node=self.root
        for cha in prefix:
            if cha in cur_node.children:
                cur_node=cur_node.children[cha]
            else:
                print('prefix wrong')
                return
        return cur_node
        
##test case
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if not prefix:
        return
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

##test cases:
f('fas') ## not found
f('')  ## None
f('a') ###[nt nthology ntagonist ntonym]
f(None)
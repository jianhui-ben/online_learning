import sys
import queue ## priority queue

class HuffmanNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def huffman_encoding(data):
    freq= {}
    for i in data:
        freq[i]=freq.get(i,0)+1
    freq_list=[]
    for key, value in freq.items():
        freq_list.append((value,key))  ## e.g. (3, A), (4, B)

    p = queue.PriorityQueue()  ## use a priority queue to track the progress of huffman tree built-up
    rank=0
    for value, key in freq_list:    # 1. Create a leaf node for each symbol
        rank +=1
        p.put((value, rank, key))             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], rank, node)) # 2c. add new node to queue
        rank+=1
    tree= p.get()
    match_dic={}
    code=''
    def dfs(tree, code):  ## traverse the tree and get the code for each leaf node
        node= tree[2]
        if isinstance(node, str):
            match_dic[node]= code
        else:
            dfs(node.left, code+'0')
            dfs(node.right, code+'1')
    dfs(tree, code)
    out=''
    for i in data:
        out+=match_dic[i]
    return out, tree


def huffman_decoding(data,tree):
    out=''
    node= tree[2]
    while len(data)>0:
        if data[0]=='0':
            if not isinstance(node.left[2], str):
                node=node.left[2]
            else:
                out+=node.left[2]
                node=tree[2]
        else:
            if not isinstance(node.right[2], str):
                node=node.right[2]
            else:
                out+=node.right[2]
                node=tree[2]
        data=data[1:]
    return out

##test cases
assert huffman_encoding('A')[0]==''
assert huffman_encoding('')[0]==''
assert huffman_encoding('AACCCC')[0]=='001111'
assert huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')[0]=='1010101010101000100100111111111111111000000010101010101' 
##test long string
large_str='a'*100+'b'*200 +'c'*1000
huffman_encoding(large_str)[0]

a,b=huffman_encoding('The bird is the word')
assert huffman_decoding(a, b)=='The bird is the word'

a,b=huffman_encoding('I like basketball')
assert huffman_decoding(a, b)=='I like basketball'

a,b=huffman_encoding('nothing to lose')
assert huffman_decoding(a, b)=='nothing to lose'

a,b=huffman_encoding('AAAAAAA  BBB')
assert huffman_decoding(a, b)=='AAAAAAA  BBB'

a,b=huffman_encoding('  BB CC  DD')
assert huffman_decoding(a, b)=='  BB CC  DD'

a,b=huffman_encoding(large_str)
assert huffman_decoding(a, b)==large_str

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



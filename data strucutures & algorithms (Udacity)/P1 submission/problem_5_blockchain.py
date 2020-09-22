import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
   
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.data).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block {}".format(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

## test case 1 empty chain
MyBlockChain = []
MyBlockChain.append(Block(0, datetime.now(), "Genesis Block", "0"))


## test case 2
for i in range(0,10):
    MyBlockChain.append(next_block(MyBlockChain[-1]))

### See the sample block chain:
for item in MyBlockChain:
    print(item.data)


## test case 3: large number
for i in range(10, 1000):
    MyBlockChain.append(next_block(MyBlockChain[-1]))

### See the sample block chain:
for item in MyBlockChain:
    print(item.data)
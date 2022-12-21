import hashlib
import datetime

#Creation of a block

class Block :
    def __init__(self,  block_number, transactions, previous_block_hash, timestamp):
        self.block_number = block_number
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions 
        self.timestamp = timestamp
        self.hash = self.get_hash()
        

    # staticmethod

    #Creation of the genesis Block with random Data

    def create_genesis_block():
        return(Block("0","ABC","0", datetime.datetime.now()))
     
    #Get the hash function of a Block

    def get_hash(self):
        header_bin = (str(self.block_number) + str(self.transactions) + str(self.previous_block_hash) + str(self.timestamp)).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    # Setting a new hash after mining a Block


    def set_hash(self,hash):
        self.hash = hash

    def add_Nonce(self,data):
        self.transactions = self.transactions + str(data)


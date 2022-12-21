from MiningScript import mine
from Block1 import Block
import datetime


#Реализация блокчейн модели

if __name__ == '__main__':

	block_chain = [Block.create_genesis_block()]
	print("Блок #%a создан." %(0))
	print("Хэш блока #%a: %s" %(0,mine(block_chain[0],3)))

	num_blocks_to_add = 5

	for i in range(1, num_blocks_to_add + 1):
		block_chain.append(Block(i,"DATA !",block_chain[-1].hash, datetime.datetime.now()))
		block_chain[i].set_hash(mine(block_chain[i],3))
		print("Блок #%a создан." %i)
		print("Хэш блока #%a: %s" %(i,block_chain[i].hash))


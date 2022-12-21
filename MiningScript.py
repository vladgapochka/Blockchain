from hashlib import sha256
from Block1 import Block

import datetime

#Рандомный MAX_Nonce

MAX_Nonce = 100000

#Метод криптографии

def SHA256(text) : 
	return sha256(text.encode("ascii")).hexdigest()


#Функция для майнинга (наличие доступа для проверки текущего блока и получение вознаграждения)
#переменная prefix_zeros - это количество нулей, требуемое в новой хэш-функции текущего добытого блока

def mine(Block, prefix_zeros):

	prefix_str = '0'*prefix_zeros

	for nonce in range(MAX_Nonce):
		# добавление к блоку транзакцию
		Block.add_Nonce(nonce)
		#новый хэш
		new_hash = Block.get_hash()
		if new_hash.startswith(prefix_str):
			print('Блок успешно добыт, его значением : ' + str(nonce))
			return(new_hash)
	raise print("Не удалось найти правильное решение после попытки" + str(MAX_Nonce) + "times")
		


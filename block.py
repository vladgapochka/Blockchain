import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'

# Получаем фаил
def get_files():
    files = os.listdir(blockchain_dir)
    for i in range(len(files)):
        files[i] = int(files[i])
    return files


#Хэширование md5
def get_hash(filename):
    file = open(blockchain_dir + str(filename), 'rb').read()
    return hashlib.md5(file).hexdigest()


# Проверка целостности блоков
def check_integrity():
    # 1. Считать хэш предыдущего блока
    # 2. Заново вычислить хэш предыдущего блока
    # 3. Сравнить эти хэши
    files = get_files()
    files = sorted(files)
    flag = True
    results = []
    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']

        prev_file = (file-1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash and flag == True:
            res = 'OK'
        else:
            res = 'Блок повреждён'
            flag = False
        results.append({'block': prev_file, 'result': res})
    return results


# Добавление блока
def write_block(name, amount, to_whom, prev_hash=""):
    files = get_files()

    last_file = sorted(files)[-1]
    prev_hash = get_hash(str(last_file))
    filename = str(last_file + 1)

    data = {
        "name": name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': prev_hash
    }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    check_integrity()


if __name__ == '__main__':
    main()
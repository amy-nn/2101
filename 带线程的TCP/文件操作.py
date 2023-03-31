import os.path

if __name__ == '__main__':
    size1 = os.path.getsize('客户端/a.txt')
    print(size1)

    print(os.path.exists('b.txt'))  #True存在  False不存在
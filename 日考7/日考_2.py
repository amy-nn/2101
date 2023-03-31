import threading


def sell_ticket(n):
    with open('ticket.txt', 'r') as f:
        old = int(f.read())

    if old > 0 and old >=n:  #保证不出负数
        old -= n

        with open('ticket.txt', 'w') as f:
            f.write(f'{old}')
        print(f'{threading.currentThread().name}-票数：{old},购买成功')
        return 1
    else:
        print(f'{threading.currentThread().name}-票数：{old},购买失败')
        return 0

if __name__ == '__main__':

    for i in range(50):
        thread1 = threading.Thread(target=sell_ticket, args=(1,))
        thread1.start()
        thread1.join()  # 不能串行实现，只能上锁




#1主进程1主线程
import threading

#全局变量（可以让多个线程来共享）
money = 0  #饮水机
#串行 join()
#上锁

def save_money():
    global money  #修改全局变量必须加个global
    lock.acquire() #上锁 关门
    for i in range(1000000):
        money +=1
    print(f'线程的名字：{threading.currentThread().name}--{money}')
    # lock.release()  #解锁 开门  死锁

def get_money():
    global money  #修改全局变量必须加个global
    lock.acquire()  # 上锁 关门
    for i in range(1000000):
        money -=1
    print(f'线程的名字：{threading.currentThread().name}--{money}')
    lock.release()  # 解锁 开门

if __name__ == '__main__':

    lock = threading.Lock()  #创建了一个锁对象
    # lock.acquire()上锁  lock.release()解锁

    #存钱
    thread1 = threading.Thread(target=save_money)
    thread1.start()
    # thread1.join()

    #取钱
    thread2 = threading.Thread(target=get_money)
    thread2.start()
    # thread2.join()

    #由于多个线程可以共享同一个数据(money)，线程的执行无序会出现脏数据（不对的数据）
    #如何解决脏数据的问题：1.join()串行   2.锁对象





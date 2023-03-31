import multiprocessing


def show1():
    for i in range(100):
        print('show1')


if __name__ == '__main__':
    # 守护进程  销毁进程
    s1 = [1, 2, 3]
    a = s1[0]  #1

    #主进程
    print('this is 主进程')

    pro1 = multiprocessing.Process(target=show1)
    pro1.daemon = True #子守护主，主运行完了子也跟着结束
    pro1.start()
    # pro1.join()
    # pro1.terminate()  #销毁进程  kill





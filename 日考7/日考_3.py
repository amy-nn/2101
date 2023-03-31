import multiprocessing
import threading



if __name__ == '__main__':



    pro1 = multiprocessing.Process(target=show)
    pro1.start()
    pro1.join()

    thread1 = threading.Thread(target=show)
    thread1.start()
    thread1.join()
import time

def cost_time(fn):
    def inner(*args,**kwargs):  #1.参数通用
        start = time.time()
        num = fn(*args,**kwargs)  #2.返回值通用
        end = time.time()
        print(f'花费的时间是{end-start}')
        return num    #3在inner里多个return
    return inner

def logging(fn):  #show()
    def inner(*args,**kwargs):
        num = fn(*args,**kwargs)
        with open('月考3_日志.txt','w') as f:
            f.write(f'{num}')
        return num
    return inner




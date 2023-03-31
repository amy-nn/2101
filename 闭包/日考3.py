# retry
import random
import time


def retry(fn):  #被装饰的函数  fn = my_random
    def inner(*args,**kwargs):  #my_random(*args,**kwargs)
        for i in range(5):
            fn(*args,**kwargs)  #调用函数  my_random(*args,**kwargs)
            print(len(args)+len(kwargs))  #获得参数的长度-- 0
            print(fn.__name__)  #my_random
    return inner

#被装饰的函数
@retry
def my_random():
    num = random.randint(1,10)
    if num <=5:
        print(f'{num}生成成功')
    else:
        print(f'{num}失败')
        with open('数字.txt','a') as f:
            f.write(f'{num}\n')
        time.sleep(3)
if __name__ == '__main__':
    my_random()

    # '王嘉轩'.endswith('王')
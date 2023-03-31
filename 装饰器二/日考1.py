is_login = False #登录
has_priv = True #权限

#判断登录
def check_login(fn):
    if is_login == False:
        print('先登录')
    def inner(*args,**kwargs):

        if is_login and has_priv:
            print('处于登录状态')
            fn(*args,**kwargs)
    return inner

def check_priv(fn):
    if has_priv == False:
        print('无权限访问')
    def inner(*args, **kwargs):
        if  is_login and has_priv:
            print('有权限')
            fn(*args, **kwargs)
    return inner

@check_priv
@check_login
def index():
    print('我准备登录了，判断一下是否可以登录')

if __name__ == '__main__':
    index()
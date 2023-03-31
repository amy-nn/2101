def make_p(fn):
    def inner(*args,**kwargs):
        num = fn(*args,**kwargs)
        # print(f'<p>{num}</p>') #hello

        return f'<p>{num}</p>'
    return inner

def make_quote(fn):
    def inner(*args,**kwargs):
        num = fn(*args,**kwargs)
        print(f'<quote>{num}</quote>')  # hello
        return num
    return inner

@make_quote
@make_p
def show():
    return 'hello'

if __name__ == '__main__':
    show()
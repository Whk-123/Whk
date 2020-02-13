'''
带参数的装饰器有3层
比起没有参数的装饰器，其最外层添加了一个函数，用来接收装饰器参数

'''


def decorate(a):                   #第一层，接收装饰器参数

    def decorate1(x):                #第二层，接收函数

        print('外层测试1')

        def wrapper1(*args, **kwargs):       #第三层，接收函数的参数
            x(*args, **kwargs)
            print('第一次装饰中……')
            print('第一次装饰完成！，共花费了{}亿元'.format(a))

        print('外层测试2')
        return wrapper1             #返回    第三层的函数名
    return decorate1             #返回   第二层的函数名

@decorate(100)
def house():
    print('房子太简陋了，需要装修！')

house()

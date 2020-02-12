'''
将商品添加进购物车后验证有没有登录，没有的登录，有则将商品添加进购物车
'''

def add_ShoppingCart(goods_name):
    if online == 0:
        print('您还没有登录，请登录')
        login_ing()                     #返回登录
    else:

        ShoppingCart.append(goods_name)
        print("{}已添加进购物车！".format(goods_name))
        print("你的购物车内有：", ShoppingCart)
        answer = input('是否继续购物？y/n  \n')
        if answer == 'y':
            shopping()            #返回购物


def login(username, password):
    user = '123'
    passw = '123'

    if username == user and password == passw:
        print("登录成功")
        global online
        online = 1
        add_ShoppingCart(goods_name1)       #登录成功将商品添加进购物车

    else:
        print('用户名或密码错误！')
        login_ing()


def login_ing():

    username1 = input('请输入用户名：')
    password1 = input('请输入密码：')
    login(username1, password1)


def shopping():
    global goods_name1
    goods_name1 = input("你要购买什么商品？ \n")
    add_ShoppingCart(goods_name1)

ShoppingCart=[]
online = 0
shopping()


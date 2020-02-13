import random
import time


def login(username, password):
    user = '123'
    passw = '123'
    print('登录中……')
    time.sleep(2)
    if username == user and password == passw:
        print("登录成功")
        global online
        online = 1
        add_ShoppingCart()

    else:
        print('用户名或密码错误！')
        login_ing()


def code_login(n):
    code_database = '123456789qwertyuiopasdfhjgxcvnQUIYFMZBVL'
    code = ''
    for i in range(n):
        ind = random.randint(0, len(code_database) - 1)
        code += code_database[ind]
    return code


def login_ing():
    username1 = input('请输入用户名：')
    password1 = input('请输入密码：')
    code1 = code_login(5)  # 5位验证码
    print('验证码：', code1)
    code2 = input('请输入验证码： ')
    if code1.lower() == code2.lower():
        login(username1, password1)
    else:
        print('验证码输入错误')
        login_ing()


def login_request(x):
    print('检验登录')

    def wrapper1(*args, **kwargs):
        if online == 1:
            x(goods_name1)

        else:
            print('你还没有登录,无法添加进购物车.')
            login_ing()

    return wrapper1


def shopping():
    global goods_name1
    goods_name1 = input("你要购买什么商品？ \n")

    ShoppingCart.append(goods_name1)
    if online == 1:
        add_ShoppingCart(goods_name1)


ShoppingCart = []
online = 0
shopping()


@login_request
def add_ShoppingCart(goods_name):
    print("{}已添加进购物车！".format(goods_name))
    print("你的购物车内有：", ShoppingCart)
    answer = input('是否继续购物？y/n  \n')
    if answer == 'y':
        shopping()


add_ShoppingCart()

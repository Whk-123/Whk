#[表达式 for 变量 in 旧列表 if 条件]

#过滤掉长度大于5的数
list_old = [1,22,333,4444,55555,666666,7777777,88888888,999999999]
list_new = [list1 for list1 in list_old if len(str(list1))<=5]
print(list_new)





result = [(x, y) for x in range(0, 5) if x % 2 == 0 for y in range(0, 10) if y % 2 == 1]
print(result)
#用列表推导式可以简化步骤
#result=[]
for x in range(5):
    for y in range(10):
        if x%2==0 and y%2==1:
            result.append((x,y))

print(result)


-------------------------------------------------------------
#生成器
#应用与协程
#方法：__next__() :获取下一个元素
      send(value):向每次生成器调用中传值，第一次要调用send(None)



#1
#将列表生成器的[]换成（）即是生成器

#利用循环while……方便调用

generator1 = （x for x in range(1000000)
print(type(g))          #generator
#通过__next__()得到元素
print(g.__next__())  #每调用一次得到一个元素
print(g.__next__())
#通过next()得到元素
print(next(g))            #每调用一次得到一个元素
print(next(g))


-------------------------------------------------------------
#生成器
#2
#函数中含有yield关键字，则会变成生成器
def func():
    n=0
    while True:
        n += 1
        # print(n)
        yield n           #相当于return n + 暂停，继续调用生成器会从停的位置继续

generator1 = func()
print(type(generator1))
print(next(generator1))
print(next(generator1))


'''

# 获取斐波那契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a + b
        n += 1

a = int(input('要多少个斐波那契数列？'))
g = fib(a)
for i in range(a):
    print(next(g))

'''



-----------------------------------------------------------------------
#迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
只能往前不能后退

可迭代的：生成器 列表 元组 字典 字符串 集合
但可迭代并不就一定是迭代器！！
----》生成器是可迭代的，也是迭代器
----》列表，元组，字典，字符串，集合是可迭代的，但不是迭代器
'''
list1 = [1,2,3,4,56]
print(next(list1))
print(next(list1))
#TypeError: 'list' object is not an iterator
'''


#但可以通过内置函数iter()将可迭代的列表,元组等转成迭代器
'''
list1 = [1,2,3,4,56]
f = iter(list1)
print(next(f))
print(next(f))
'''

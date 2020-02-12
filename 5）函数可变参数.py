def sum1(*args):       # *args表示可变参数
    
    a = 0
    for i in args:
        a += i
    print('和是：', a)
    
sum1()
sum1(1)
sum1(1,2,3)



-------------------------------------
def sum1(name,*q):    #sum1第一个元素赋值给name，其他的全部赋值给q
    print(name,q)     #可变参数必须放在后面，否则报错
    a = 0
    for i in q:
        a += i
    print('和是：', a)

sum1(Tom',1,4,6,7,8)

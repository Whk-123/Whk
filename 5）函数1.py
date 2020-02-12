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

     
     

     
------------------------------------------
#关键字参数
def func(**kwargs):      # key word arguments      !只接收key=value
     print(kwargs)       #{'a':1,'b':2,'c':3}   默认转成字典保存  
func(a=1,b=2,c=3)

     
---------------------------------------------
def func(**kwargs):  # key word arguments       !只接收key=value           将关键字参数装包，形成字典
    print(kwargs)    

dict1={'01':'python','02':'java','03':'c语言'}
func(**dict1)          #  ** 将字典拆包，使func('01'='python','02'='java'……)，形成关键字参数
     
------------------------------------------------------
def aaa(a, b, *c, **d):
     print(a,b,c,d)        
aaa(1,2)                # 1  2  ()  {}
     
aaa(1,2,3,4)            # 1  2  (3,4)  {}
 
aaa(1,2,x=100,y=200)    # 1  2  ()  {'x':100,'y':200}


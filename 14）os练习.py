import os

a_dir = 'F:\python\p1'
b_dir = 'F:\python\p2'


def copy(a, b):
    if os.path.isdir(a) and os.path.isdir(b):
        list1 = os.listdir(a)
        print('h')

        for i in list1:
            c = os.path.join(a, i)
            c1 = os.path.join(b, i)
            if os.path.isdir(c):

                os.mkdir(c1)
                copy(c,c1)
            else:
                with open(c, 'rb') as read1:
                    read2 = read1.read()
                    d = os.path.join(b, i)
                    with open(d,'wb') as write1:
                        write1.write(read2)

        print('复制完成！')
    else:
        os.mkdir(b)
        copy(a,b)
def delate(q):
    if os.path.isdir(q):
        list2 = os.listdir(q)
        for i in list2:
            q1 = os.path.join(q,i)
            if os.path.isdir(q1):
                delate(q1)
            else:
                os.remove(q1)
        os.rmdir(q)
        print('删除完成')

#copy(a_dir, b_dir)           #复制p1文件夹内的文件到p2文件夹
delate(b_dir)               #删除p2

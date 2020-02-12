#列表排序函数
def sort1(ele):
    if isinstance(ele,list):
        for i in range(len(ele)-1):
            for j in range(len(ele)-1-i):
                if ele[j]>ele[j+1]:
                    ele[j],ele[j+1]=ele[j+1],ele[j]
                    print(list1)

list1 = [3,5,46,63,25,8769,3]
sort1(list1)
'''
'''
#列表翻转函数
def reverse1(ele):
    if isinstance(ele,list):
        for i in range(len(ele)-1):
            if i <= (len(ele)/2):
                ele[i],ele[len(ele)-i-1] = ele[len(ele)-i-1],ele[i]
                print(ele)

list1 = [3,5,46,63,25,8769,55]
reverse1(list1)
'''

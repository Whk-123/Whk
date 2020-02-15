class SalarySystem:
    def __init__(self, idnumber, name):
        self.__idnumber = idnumber
        self.__name = name

    @property
    def idnumber(self):
        return self.__idnumber

    @idnumber.setter
    def idnumber(self, id1):
        self.__idnumber = id1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name1):
        self.__name = name1


class Worker(SalarySystem):
    def __init__(self, idnumber, name, salary):
        super().__init__(idnumber, name)
        self.salary = salary * 10 * 20  # 工人薪水,一天10小时，每小时100块
        list1.append({self.name: self.salary})

    def __str__(self):
        return '{}的id是{}，职位是工人,每月的薪水是{}'.format(self.name, self.idnumber, self.salary)


class Salesman(SalarySystem):
    def __init__(self, idnumber, name, sale):
        super().__init__(idnumber, name)
        self.sale = sale * 0.3  # 销售员薪水,销售额*提成比例30%
        list1.append({self.name: self.sale})

    def __str__(self):
        return ('{}的id是{}，职位是工人,每月的薪水是{}'.format(self.name, self.idnumber, self.sale))


class Manager(SalarySystem):
    def __init__(self, idnumber, name, salary):
        super().__init__(idnumber, name)
        self.salary = salary  # 经理薪水,固定月薪
        list1.append({self.name: self.salary})

    def __str__(self):
        return ('{}的id是{}，职位是工人,每月的薪水是{}'.format(self.name, self.idnumber, self.salary))


class Salemanager(SalarySystem):
    def __init__(self, idnumber, name, salary, sale):
        super().__init__(idnumber, name)
        self.salary = salary
        self.sale = sale * 0.3
        list1.append({self.name: self.salary + self.sale})

    def __str__(self):
        return ('{}的id是{}，职位是工人,每月的薪水是{}'.format(self.name, self.idnumber, self.salary + self.sale))


list1 = []
#工人
a1 = int(input('你是工人，你这个月工作了多少天？'))
worker = Worker(2020001, '张三', a1)
print(worker)
print(worker.name)  # 获取姓名
print(worker.idnumber)  # 获取员工号

#销售员
a2 = int(input('你是销售员，你这个月的销售额是多少？'))
salesman = Salesman(2020002, '李四', a2)
print(salesman)

#经理
a3 = int(input('你是经理，你的固定月薪是多少？'))
manager = Manager(2020003, '李四', a3)
print(manager)

#销售经理
a4 = int(input('你是销售经理，你的固定月薪是多少？'))
a5 = int(input('你是销售经理，你这个月的销售额是多少？'))
salesmanager = Salemanager(2020004, '李四', a4, a5)
print(salesmanager)

print('所有人的工资情况：')
print(list1)

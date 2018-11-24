'''
 函数名()  # 调用函数
# # 方法名()  # 调用方法
# # 类名()  # 创建对象
'''
# class People:
#     name = 'xiaoming'
#     age = 18
#     def eat(self,num):
#         print('吃')
#         return '123'
#     def say_hello(self):
#         print('%s 说sayhello 今年 %d岁了' %(self.name,self.age))
# xiaoming = People()
# print(xiaoming.name)
# xiaoming.name = '小明'
# xiaoming.age = 5
# xiaoming.say_hello()
# class Dog:
#     name = ''
#     varity = ''
#     def eat(self):
#         print('%s 吃狗粮' % (self.name))
#     def dark(self):
#         print('%s 汪汪汪' % (self.varity))
#
# dog1 = Dog()
# dog1.name = '燕窝'
# dog1.varity = '哈士奇'
# print(dog1.name)
# dog1.eat()
# dog1.dark()
###     self方法
# class Person:
#     name = '小明'
#     def __init__(self,name):
#         self.name = name
#         self.age = 12
#         self.position = [1,2]
#         self.bounds = '1234'
#     def __str__(self):
#         print('name = %s,age = %s,position = %s,bounds = %s' %(self.name,self.age,self.position,self.bounds))
#     def __int__(self):
#         self.name = 'xiaoming'
#     def say_hello(self):
#         print('%s你好'%self.name)
# p1 = Person('xiaoming')
# p1.say_hello()
# p2 = Person('xiaohong')
# p2.name = '小红'
# p2.say_hello()
class Bank:
    def __init__(self):
        self.__bance = 100
    def bank_get(self,num):
        self.__bance = num
    def bank_set(self):
        print('您的余额为%d' % self.__bance)
bk = Bank
bk.bank_set()
bk.bank_get()









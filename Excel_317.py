# def test(fn):
#     print("注册")
#     print("登录")
#     fn()  #参数可以是调用函数
# # test()
# def test01():
#     print("发信息")
# test(test01)
# def send():
#     print("发送消息")
# # send()
# def outer(fn):
#     def inner():
#         print("登录")
#         fn()
#     return inner()  闭包函数
# # print(outer(send))
# ot=outer(send())
# ot()
# def outer(fn):
#     def inner():
#         print("登录")
#         fn()
#     return inner()
# @outer    #语法糖  装饰器函数  把下面这个函数放到闭包函数里面
# def send():
#     print("哈哈哈")
# send()
# def outer():
# #     def inner(name):
# #         print(f"{}")
# class 类名：     #基本格式
#     代码块
# class Washier:
#     height=800
# # print(Washier.height)
# # Washier.width=450
# # print(Washier.width)
# wa=Washier()
# print(wa)
# wa1=Washier()
# print(wa1)
# name=list(range(1,9))
# print(name)
# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
# squares=[value**2 for value in range(1,11)]
# print(squares)
# for i in  range(1,21):
#     print(i)
# name=list(range(1,10000001))
# print(min(name))
# print(max(name))
# print(sum(name))
# # for i in  name:
# #     print(i)
# shuzi=[value for value in range(1,21,2)]
# for i in shuzi:
#     print(i)
# shuzi=[value**3 for value in range(1,11)]
# for i in shuzi:
#     print(i)
# class person:
#     name="guoguo" #属性
#     def run(self):  #方法
#         print("run 中的self")
#         print("跑步")
# pe=person()   #实例化对象
# print(pe)
# pe.run()  #类的方法
# class person:
#     name="果果"
#     def introduce(self):   #实例属性
#         print(f"{person.name}的年龄：{self.age}")
# pe=person()   #使这个对象调用出来
# pe.age=18   #实例属性   #私有的 不能由类访问
# pe.introduce()
# pe.sex="男" #效率低
# __init__()初始化 赋值操作  会被自动调用
# class test:
#     def __init__(self):
#         print("函数")
# te=test()
# class person:
# #     name="xx"  #类属性
# #     def __init__(self):    #有self 就是实例属性
# #         self.name="guoguo"
# #         self.age=186
# #         self.height=199
# #     def play(self):
# #         print(f"{self.name}打王者荣耀")
# #     def introduc(self):
# #         print(f"{self.name}年龄是{self.age}身高{self.height}")
# # # pe=person()
# # # pe.play()
# # # pe.introduc()
# # # pe2=person()
# # # pe2.play()
# # # pe2.introduc()
# class person:
#     name="xx"  #类属性
#     def __init__(self,name,age,height):    #有self 就是实例属性   self 代表pe2
#         self.name=name   #传参数
#         self.age=age
#         self.height=height
#     def play(self):
#         print(f"{self.name}打王者荣耀")
#     def introduc(self):
#         print(f"{self.name}年龄是{self.age}身高{self.height}")
# # pe=person("guo","18","199")
# # pe.play()
# # pe.introduc()
# pe3=person("shu",19,199)  #依次传入
# pe3.play()
# pe3.introduc()
# class Person:
#     def __init__(self):
#         print("执行")
#     def __del__(self):
#         print("销毁")
# pe=Person()
#    #语句被执行的时候   对象已经被删除了
# print("sssssss")   #正常运行不会去调用  del   最后才去执行的东西
# print("xxxxxxxxxxx")
#1.面向对象特性   封装（只让他用不让看） 继承 多态
# class person:
#     name="bb"
# pe=person()
# print(pe.name)
# person.name="zz"
# print(person.name)   #可以更改
# class person:
#     name="GG"  #类属性
#     __age=18    #隐藏属性
#     def introduce(self):
#         person.__age=1
#         print(f"{person.name}年龄是{person.__age}")
# pe=person()
# print(pe.name)
# # print(pe.age)  #访问不了 名字改了 __age=_person__age   _类名__属性名
# # print(pe._person__age)
# # pe._person__age=1
# # print(pe._person__age)
# print(pe.introduce())
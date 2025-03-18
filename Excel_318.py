# class person:
#     name="guoguo"
#     __age=54   #隐藏属性
#     _sex='nan'    #私有
# pe=person()
# print(pe._sex)
# print(pe._person__age)
# class Man:
#     def __play(self):
#         print("玩手机")
#     def funa(self):
#         print("yiban")
#         # Man.__play(self)
#         self.__play()
# man=Man()
# man.funa()
# # man._Man__play()
# class girl:
#     def buy(self):
#         print("买")
# g=girl()
# g.buy()
# class dog:#单继承多继承#继承 子类默认继承父类所有方法
#     def eat(self):
#         print("chi")
#     def sing(self):
#         print("chang")
# class girl(dog):           #继承了
#     pass
# g=girl()
# g.eat()
# g.sing()
#ABC  c继承b  b 继承a"
# class father:
#     def eat(self):
#         print("吃")
#     def sleep(self):
#         print("睡")
# class son(father):#单继承
#     pass
# class grandson(son):   #父类的所有方法   多重继承
#     pass
# s=grandson()
# s.eat()
# s.sleep()
# 方法重写
# class person:             #父类
#     def money(self):
#         print("家里钱")
# class man(person):     #子类
#     def money(self):
#         # person.money(self)
#         super().money()
#         print("自己赚钱")
# m=man()
# m.money()
# aliens=[]
# for alien_numeber in  range(30):
#     new_alien={"color":"green","point":"5","point":5}
#     aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien["color"]=="green":
#         alien["color"]="yellow"
#         alien["speed"]="medium"
#         alien["points"]=10
# for aliens in aliens[:5]:
#     print(aliens)
# print("....")
# pizza={
#     "crust":["thick","big","python"],
#     "toppings":["mushrooms","extra cheese"],
#     "small":["1","2","3"]
#        }
# for name,languages in pizza.items():
#     print("my name is "+name+"'s favorite languages are: ")
#     for topping in languages:
#         print(topping)

# s=input("请输入姓名")
# print(f"hi,{s}")
#我的邮件
# s=input("输入姓名：")
# b=input("输入产品名：")
# print(f"Dear {s}: Your purchased product : {b}is delivered! Thanks for your choosing!")
#他的邮件答题
# email_template="""Dear %s:
#
# Your purchased product : %s is delivered!
#
# Thanks for your choosing!"""
# name=input("请输入名字：")
# product=input("请输入产品：")
# email=email_template%(name,product)
# print(email)
#字符串的截取
# str="You Rise Me Up"
# print(str[4:8])
#大写转为小写
# str="Python Basic"
# print(str.lower())
# a=1000
# b=2000
# c=1000000
# print(a*b-c)
# print(type(100))
# print(type("hallo"))9
# 月份判断
# mon=int(input("请输入："))
# if 1<=mon<=3:
#     print("春")
# elif 4<=mon<=6:
#     print("sta")
# elif 7<=mon<=9:
#     print("atu")
# elif 10<=mon<=12:
#     print("win")
# else:
#     print("输入1-12的月份")
# month=int(input("请输入："))
# if month<1 or month >12 :
#     print("输入无效")
# else:
#     if month<4:
#         print("春")
#     elif month<7:
#         print("夏")
#     elif month<10:
#         print("秋")
#     else:
#         print("冬")
# name=str(input("请输入："))
# if name=="A":
#     price=int(input("请输入降价："))
#     if price>=30:
#         print(f"A+{price}")
#     else:
#         print("No Alert!")
# elif name=="B":
#     price = int(input("请输入降价："))
#     if price>=20:
#         print(f"B+{price}")
#     else:
#         print("No Alert!")
# elif name=="C":
#     price = int(input("请输入降价："))
#     if price>=10:
#         print(f"C+{price}")
#     else:
#         print("No Alert!")
# else:
#     print("No Alert!")

# name=str(input("请输入："))
# price=int(input("请输入降价："))
# # if name=="A" and price>=30:
# #     print("[alert]produc%s，price%d"%(name,price))
# # elif name=="B" and price>=20:
# #     print("[alert]produc%s，price%d"%(name,price))
# # elif name=="C" and price>=10:
# #     print("[alert]produc%s，price%d"%(name,price))
# if (name=="A" and price>=30)or(name=="B" and price>=20)or(name=="C" and price>=10):
#     print("[alert]produc%s，price%d"%(name,price))
# else:
#     print("No Alert!")

import pandas as pd
#读写文件
word=pd.read_excel("shuju.xlsx")
#分列
word["year"]=word["货主1"].apply(lambda x:x.split("/")[0].strip())
word["country"]=word["货主1"].apply(lambda x:x.split("/")[1].strip())
word["num"]=word["货主1"].apply(lambda x:x.split("/")[2].strip())
word["num2"]=word["货主1"].apply(lambda x:x.split("/")[3].strip())
# print(word[word["货主"]=="参半"])   #货主那一列等于参半
#筛选   分货主分类
# print(word["货主"].unique())

writer = pd.ExcelWriter("temp.xlsx")
for i in word["货主"].unique():
    word[word["货主"]==i].to_excel(writer,sheet_name=i)   #根据筛选的创建分表
# writer.close()
# print(word[word["包装"].str.contains("五")])

word.to_excel(writer,sheet_name="wu")
# writer.close()
word.to_excel(writer,sheet_name="原始数据")
writer.close()
#定义实现差分编码的方法函数，使用循环遍历数组的方法
def encode(list):
    arr_list=[]#在for循环外面定义一个最终返回的结果数组
    for i in range(len(list)):
        arr=[]#初始化一个数组列表
        for j in range(len(list[i])):
            if j>0:
                arr_result=list[i][j]-list[i][0]#以每行的首列为参考，用其他数值减去每行首列数值
            else:
                arr_result=list[i][j]
            arr.append(arr_result)#将结果加到arr空数组中
            if j==len(list[j])-1:#这一步是定义输出j==每行的最后一次时的结果，如果不加这一步，那for循环，每遍历一次就会输出一次
                arr_list.append(arr)
    return arr_list

#定义解码方法，同编码(encode)的方法一样，只是把之前减去的加上去就行
def unencode(list):
    arr_list=[]
    for i in range(len(list)):
        arr_1=[]
        for j in range(len(list[i])):
            if j>0:
                arr_result1=list[i][j]+list[i][0]
            else:
                arr_result1=list[i][j]
            arr_1.append(arr_result1)
            if j==len(list[j])-1:
                arr_list.append(arr_1)
                #print(arr_1)
    return arr_list

#定义数组求和方法函数,同遍历数组一样，只是结果为所有元素之和
def sum_list(list):
    sum_result=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            sum_result+=list[i][j]
    return sum_result

#定义输入数组
print("请输入数组的大小：")
n=int(input())#定义数组的行列大小
print("输入要进行差分编码的数组为：")
line=[[0]*n]*n#初始化一个n行n列的数组
for i in range(n):
    line[i]=input().split(" ")#每行中以空格隔开每个元素,不同的行则用回车隔开
    line[i]=[int(j) for j in line[i]]#把输入的数组每个元素都整型化
print("输入的数组为：",line)
#执行的结果显示
print("差分编码后的结果为：")
en_result=encode(line)
print(en_result)
print("解码后的结果为：")
unen_result=unencode(en_result)
print(unen_result)
#计算压缩比
sum_result1=sum_list(unen_result)#原来数组的和
print("原数组总和为：",sum_result1)
sum_result2=sum_list(en_result)#压缩后数组和
print("压缩后数组总和为：",sum_result2)
result=(sum_result1-sum_result2)/sum_result1
print("编码压缩比为：",result)

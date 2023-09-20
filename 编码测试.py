#定义实现差分编码的方法函数，使用循环遍历数组的方法
def encode(list):
    arr_list=[]#定义用来存储结果数组的空数组
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

arr_test=[[1,2,3],[4,5,6],[7,8,9]]
list1=encode(arr_test)
print(list1)
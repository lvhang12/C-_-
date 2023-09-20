#定义解码方法
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

arr_test=[[1,2,3],[4,5,6],[7,8,9]]
list1=unencode(arr_test)
print(list1)
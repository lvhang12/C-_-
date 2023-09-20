#定义数组求和方法函数,同遍历数组一样，只是结果为所有元素之和
def sum_list(list):
    sum_result=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            sum_result+=list[i][j]
    return sum_result
#定义两个测试数组
arr1=[[1,2,3],[4,5,6],[7,8,9]]
arr2=[[1,1,2],[4,1,2],[7,1,2]]
sum_arr1=sum_list(arr1)
print("原来的数组总和为：",sum_arr1)
sum_arr2=sum_list(arr2)
print("压缩后的数组总和为：",sum_arr2)
result=(sum_arr1-sum_arr2)/sum_arr1
print("编码后的压缩比为：",result)
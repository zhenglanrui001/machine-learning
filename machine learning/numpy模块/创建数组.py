import numpy as np

#方法一：列表转数组
arr = np.array([10, 20, 30, 40, 50])
print(arr)

#设置数组维度 ndmin
arr = np.array([10, 20, 30, 40, 50], ndmin=2)
print(arr)
print()

#数组数据类型转换 dtype
arr = np.array([10, 20, 30, 40, 50], dtype = complex)
print(arr)
print()

#数组的属性：数据类型 dtype、大小 shape
list1 = [[101, 202, 303], [404, 505, 606]]
arr1 = np.array(list1)
print("数组arr1的数据类型是:", arr1.dtype)
print("数组arr1的大小是：", arr1.shape)
print()

#全零数组 zeros(shape = (x,x), dtype)
arr0 = np.zeros((3,4))
print(arr0)

arr0 = np.zeros(shape=(2,3), dtype=int)
print(arr0)
print()

#全1数组 ones(shape = (x,x), dtype)
arr1 = np.ones((3,2),int)
print(arr1)
print()

#单位矩阵 eye(x, dtype)、 identity(x, dtype)
arr2 = np.eye(5, dtype = int)
print(arr2)
print()
arr3 = np.identity(5, dtype = int )
print(arr3)
print()

#未初始化的空数组 empty(shape=(x,x))
arr4 = np.empty((3,4))
print(arr4)

print(np.empty((2,2)))  #结果因内存状态有异
print()

#数据类型转换 astype()  !无论如何都会生成新的数组
arr = np.array([10.1, 20.2, 30.3, 40.4, 50.5])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)
str_arr = arr.astype(str)
print(str_arr)
print(str_arr.dtype)
print()

#方法二：生成随机数组 random
#标准正态分布样本数组 random.normal()
samples = np.random.normal(size=(4, 4))
print(samples)
print()

from random import normalvariate
import time
n = 1000000
start = time.time()
samples = [normalvariate(0,1) for i in range(n)]
times = np.random.normal(size=n)
end = time.time()
print(end-start)
print()

#数组的矢量化
list5 = [[101, 202, 303], [404, 505, 606]]
arr5 = np.array(list5)
multi_arr = arr5 * arr5
sub_arr = arr5 - arr5
print("乘法运算：")
print(multi_arr)
print("减法运算：")
print(sub_arr)

#广播：标量值（10）与数组的合并运算
divide_arr = arr5 / 10
print("除法运算：")
print(divide_arr)
print()

#广播运用：
#某地周气温距平

#同一时间的距平  0-列
#四天内的7个时间点气温
weathers = np.array([[20,21,22,18,19,21,22],[18,21,23,19,18,21,13],[18,19,22,21,21,17,16],[15,18,20,19,21,17,18]])
#计算列平均值（即：四天内同一时刻气温的平均值）
print(weathers.mean(0))
#中心化处理：同一时刻的气温与对应列平均气温的偏差
meaned = weathers-weathers.mean(0)
print(meaned)
#计算偏差的均值
print(meaned.mean(0))
print()

#每一天的时间距平  1-行
weathers = np.array([[20,21,22,18,19,21,22],[18,21,23,19,18,21,13],[18,19,22,21,21,17,16],[15,18,20,19,21,17,18]])
print(weathers)
print(weathers.mean(1).reshape(4,1))
meaned = weathers - weathers.mean(1).reshape(4,1)
print(meaned.mean(1))
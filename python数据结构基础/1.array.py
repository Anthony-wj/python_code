Array = [1, 2, 3 ,4]
# 增
Array.append(5) # 在数组末尾追加元素
Array.insert(0, 0) # 在指定位置增加元素
print(Array)
# 删
Array = [5, 4, 3, 2, 1]
Array.remove(5) # 按值删除：删除第一个值为要求的元素
Array.pop(0) # 按下标删除：删除指定下标的元素，默认为删除末尾元素
print(Array)
del Array[0] # 按下标删除：删除指定下标元素，和pop类似
print(Array)

# 改
Array = [5, 4, 3, 2, 1]
Array[0] = 100 # 通过索引直接修改即可
print(Array)
# 查
print(Array[1]) # 通过索引访问指定位置的元素
if 3 in Array: # 判断数组中是否存在元素
    print(True)
print(Array.index(4)) # 获取某个元素的索引

# 反转
Array.reverse()
print(Array)

# 排序
'''
    sort函数直接在原数组进行排序
    sorted函数不对原数组进行操作，需要额外空间保存排序后的数组
'''
Array = [1, 4, 2, 5, 3]
print(sorted(Array))
Array.sort()
print(Array)
# 清空

Array.clear()

# 截取
# [beg:end:step]
Array = [1 ,2 ,3 ,4 ,5]
print(Array[0:5:2])
'''
    不能直接按数字大小来进行排序，判断条件应为直接组合还是颠倒组合更大
    每轮选出一个和任意数组合最小的数，放置末尾，进行n轮，就可以实现
    采用冒泡排序的思想来进行排序，只是判断条件不是直接比大小。

'''
nums = [10, 2]
nums = [str(i) for i in nums]
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if int(nums[j] + nums[j + 1]) < int(nums[j + 1] + nums[j]):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
s = "".join(nums)
print(s)
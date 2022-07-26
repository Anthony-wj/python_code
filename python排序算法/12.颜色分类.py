'''
    使用三个变量，less_idx  i   great_idx
    将整个列表分为三个区域：小于区、等于区、大于区
    遍历列表：
        [i] < num
'''

def quick_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    less_idx = -1
    great_idx = len(seq)
    num = 1
    i = 0
    while i != great_idx:
        if seq[i] < num:
            seq[i], seq[less_idx+1] = seq[less_idx+1], seq[i]
            less_idx += 1
            i += 1
        elif seq[i] == num:
            i += 1
        else:
            seq[i], seq[great_idx-1] = seq[great_idx-1], seq[i]
            great_idx -= 1


lst = [0, 1, 2, 2, 1, 0, 2, 0]
quick_sort(lst)
print(lst)
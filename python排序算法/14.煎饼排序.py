arr = [3, 2, 4, 1]  #  4 2 3 1  # 1 3 2 4 #3 1 2 4 # 2 1 3 4
num = len(arr)
new_list = list()
while num > 1:
    max_idx = 0
    for i in range(num):
        if arr[i] > arr[max_idx]:
            max_idx = i
    if max_idx == num-1:
        num -= 1
        continue
    if max_idx != 0:
        part = arr[:max_idx+1]
        new_list.append(max_idx + 1)
        part.reverse()
        arr[:max_idx+1] = part
    c = arr[:num]
    new_list.append(1)
    c.reverse()
    arr[:num] = c
    num -= 1
print(arr)
print(new_list)
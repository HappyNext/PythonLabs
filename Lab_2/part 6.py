arr = {0,1,2,3,4,5,6,7,8}
print(arr)

arr.add(9)
print(arr)

arr.remove(9)
print(arr)

i = 9
if i in arr:
    print(f"Елемент {i} знайдено в множині")
else:
    print(f"Елемент {i} не знайдено в множині")
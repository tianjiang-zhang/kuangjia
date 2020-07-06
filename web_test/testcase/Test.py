import random


list2 = {'a':[1,2,3,4,5,6,7,8]}
zz =['null']
for i in range(1):
    a = random.randint(1,9)
    zz.append(a)
    if zz[i] == a:
        continue

    s = a
    print(list2['a'],[a])



random.randint(0,99)


list = ["完全", 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5) #从list中随机获取5个元素，作为一个片断返回

print (slice )

print (list) #原有序列并没有改变。
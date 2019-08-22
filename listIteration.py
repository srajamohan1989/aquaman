#Given a two list (of int data type) create a third list such that should contain only odd numbers 
# from the first list and even numbers from the second list
list1 = [2,5,8,4,9,11,14]
list2 = [3,2,6,7,8]
list3 = []
for listitem in list1:
    if (listitem%2!=0):
        list3.append(listitem)
for list2item in list2:
    if(list2item%2==0):
        list3.append(list2item)
print(list3)

mylist=[]
listSize=int(input("Enter List size : "))
print("Enter list elements ")
for i in range(listSize):
    mylist.append(int(input()))
print("Original List ",mylist)
mylist.insert(1,4)
print("Inserted 4 at position 1 ",mylist)
mylist.append(5)
print("Appended 5 to mylist ",mylist)
mylist.remove(2)
print("Removed First Occurance of 2 ",mylist)
mylist.sort()
print("Sorted mylist ",mylist)
mylist.pop()
print("After Poping ",mylist)
mylist.reverse()
print("After reversal ",mylist)
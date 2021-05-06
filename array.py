n=[1,2,3,4,5]
print("Original Array: ")

for i in n:
    print(i, end=" ")
print()

n= n[:: -1]

print("Array com ordem inversa: ")

for i in n:
    print(i, end=" ")
print()
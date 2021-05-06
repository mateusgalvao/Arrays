# Arrays
Mesmo tipo de array 
em java :
public class Arr {
    public static void main(String[] args) {
        int [] arr = new int [] {1,2,3,4,5};
        System.out.println("Original Array: ");
        for(int i = 0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        System.out.println("Array com ordem inversa: ");
    for (int i = arr.length -1; i >= 0; i--){
        System.out.print(arr[i] + " ");
        
    }System.out.println();
}
}
em python:
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

Com a saída:

Original Array: 
1 2 3 4 5 
Array com ordem inversa: 
5 4 3 2 1 

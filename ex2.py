# Creating a list of numbers
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print("Original List:", numbers)
numbers.append(55)
print("After adding 55:", numbers)
numbers.remove(25)
print("After removing 25:", numbers)
numbers.sort()
print("Sorted List:", numbers)
numbers.reverse()
print("Reversed List:", numbers)
index_of_30 = numbers.index(30)
print("Index of 30:", index_of_30)
sublist = numbers[2:6]
print("Sublist (elements from index 2 to 5):", sublist)
if 40 in numbers:
    print("40 is in the list.")
else:
    print("40 is not in the list.")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("List of fruits:", fruits)
fruits.sort()
print("Sorted fruits list:", fruits)
fruits.append("fig")
print("After adding 'fig':", fruits)
fruit_string = ", ".join(fruits)
print("Fruit names as a string:", fruit_string)
count_banana = fruits.count("banana")
print("Banana appears", count_banana, "times in the list.")

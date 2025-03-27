#Author: Moleboheng Madela
#Date: 2025-03-27
#Description: This program creates and manipulate lists.

#1. Creating an empty list called my_list:
my_list = []

#2. Appending 10, 20, 30, 40 to my_list:
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Check what's in my_list post appending:
print("my_list now has the values: ", my_list)

#3. Inserting 15 at index 1:
my_list.insert(1, 15)

#Check what's in my_list post inserting:
print("my_list after inserting 15 at index 1: ", my_list)

#4. Extending my_list with [50, 60, 70]:
my_list.extend([50, 60, 70])

#Check what's in my_list post extending:
print("my_list after extending with [50, 60, 70]: ", my_list)

#5. Removing the last element from my_list:
my_list.pop()

#Check what's in my_list post removing the last element:
print("my_list after removing the last element: ", my_list)

#6. Sorting my_list in ascending order
my_list.sort()

#Check what's in my_list post sorting:
print("my_list after sorting in ascending order: ", my_list)

#7. Print my_list index with the value of 30:
#FIrstly: Find the index of 30
index_val30 = my_list.index(30)

#Secondly: Print the index of 30
print("Index for the value of 30 in my_list is: ", index_val30)
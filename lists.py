# an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Removes the last element
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)

print("Index of 30:", index_of_30)

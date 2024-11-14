Slip 4
# Q.1) Write a program to implement different Set Operations (any 5 operations)

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print("Set A:", setA)
print("Set B:", setB)

union_set = setA | setB
print("\n1. Union of A and B:", union_set)

intersection_set = setA & setB
print("2. Intersection of A and B:", intersection_set)

difference_set = setA - setB
print("3. Difference of A - B:", difference_set)

symmetric_diff = setA ^ setB
print("4. Symmetric Difference of A and B:", symmetric_diff)

is_subset = setA <= setB
print("5. Is A a subset of B?", is_subset)

is_superset = setB >= setA
print("6. Is B a superset of A?", is_superset)

setA.add(9)
print("7. Set A after adding element 9:", setA)


Output:
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}

1. Union of A and B: {1, 2, 3, 4, 5, 6, 7, 8}
2. Intersection of A and B: {4, 5}
3. Difference of A - B: {1, 2, 3}
4. Symmetric Difference of A and B: {1, 2, 3, 6, 7, 8}
5. Is A a subset of B? False
6. Is B a superset of A? False
7. Set A after adding element 9: {1, 2, 3, 4, 5, 9}

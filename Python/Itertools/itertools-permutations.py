from itertools import permutations

list1 = (list(input().split()))
list2 = list(sorted(permutations(list1[0], int(list1[1]))))
print("\n".join(["".join(x) for x in list2]))


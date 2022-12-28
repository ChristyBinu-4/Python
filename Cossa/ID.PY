a = [[1,"slice",3],[2,"show",3]]
a.append(['a','b','c'])
a.extend(["f","g","h"])
a.insert(1,[3,4,5])
b = [4.1,3.5,2,9,3.1]
b.sort()
b.reverse()
a.remove([3,4,5])
a.pop(2)

print(a)
print(b)
print(a.count('f'))
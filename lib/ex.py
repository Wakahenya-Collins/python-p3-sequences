my_list = [1, 2, 3, 4]
print(my_list[0])

s = [4, 6, 3, 9, 3, 5, 1, 2]
1 in s
# => True
s + s
# => [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s * 2
# => [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s[1]
# => 6
s[-1]
# => 2
s[2:5]
# => [3, 9, 3]
s[2:5:2]
# => [3, 3]
len(s)
# =>  8
min(s)
# => 1
max(s)
# => 9
s.index(3)
# => 2
s.count(9)
# => 1
print(s)
my_range = range(4)
print(my_range)
# => range(0, 4)
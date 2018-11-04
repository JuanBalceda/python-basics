# Variable (id, type, value)

abc = 100
id(abc)
type(abc)
print(type(abc), abc)

# Numeric variable
num = 59.75
num2 = int(67.90)
num3 = float(67.90)

print(num)
print(num2)
print(type(num3), num3)

# String variable
text = 'Text string in one line'
print(text)

text = "Text string in one line"
print(text)

text = "Text " \
       "string " \
       "in " \
       "one line"
print(text)

text = '''Text 
string 
in 
multiple lines'''
print(text)

# Deprecated
# concat = "Number: %s" % num2
# print(concat)

concat = "Number: {}".format(num2)
print(type(concat), concat)

# Tuple variable

tuple1 = (4, 5, 6, 8)
print(type(tuple1), tuple1)

# List variable
list1 = [5, 6, 8, 9, 4]
print(type(list1), list1)
list1.append(10)
list1.insert(0, 0)
print(type(list1), list1)

text2 = "Today is a great day"
print(text2[4:9])

# Dictionary variable

dic = dict(one=1, two=2, four=4, five="5")
for r in sorted(dic.keys()):
    print(r, dic[r])

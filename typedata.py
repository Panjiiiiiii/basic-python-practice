#string
x = "18"
print(type(x), x)
#float
x = 2.5
print(type (x), x)
#complex
x = 9+5j
print(type (x), x)
#boolean
x = True
print(type (x), x)
#data_collection(ARRAY)
x = [1, 2.2, 2+7j, 'Njoel']
print(type(x), x)
#tuple
x = (1, 2.2, 2+7j, 'Njoel')
print(type(x), x)
#set
x = {1, 2.2, 2+7j, 'Njoel'}
print(type(x), x)
#dictionary
x={'name':'njoel', 'age':20, 'student':True}
print(type(x), x)

#string hack -------------------->

multi_line = """
Hello
What are you doing
wowowoww
"""
print(multi_line)

x = 'Njoel'
print(x[0])

x = 'Panjoell'
print(x[2:])

#FORMATED STRING

#f formating
name = "John doe"
print(f"Hello my name {name}")

#%- formatting
name = "John doe"
print("Hello my name %s" %(name))

#str.dormat()
name = "John doe"
print("Hello my name {}".format(name))

#string hack -------------------->

#data_collection(ARRAY) hacks ---------->

x = [1, 2.2, 2+7j, 'Njoel']

#INDEXING
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])

#SLICING
print(x[0:5:2])
print(x[0:])
print(x[:2])

#data_collection(ARRAY) hacks ---------->

#set union & interection hacks ------------------->
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection: ", intersection)

#set union hacks ------------------->

#dictionary hacks (crud) ------------------>
x={'name':'njoel', 'age':20, 'student':True}
print(x)
#create data
x['addres'] = 'Jakarta'
print(x)
#delete data
del x['student']
print(x)
#update data
x['age'] = 33
print(x)
#dictionary hacks ------------------>

#convert data type ------------>
print(int("25"))
print(float(25))
print(str(25.0))
print(list('njoel'))
print(dict([[1,2],[3,4]]))
#convert data type ------------>

#upper & lower case -------------->
kata = 'njoel'
kata = kata.upper()
print(kata)

kata = 'NJOEL'
kata = kata.lower()
print(kata)
#upper & lower case -------------->

#operation list, set and string -------------->
#len()
list_example = [1,3,4,5,5,67,7]
print(list_example)
print(len(list_example))

set_example = set([1,2,3,4,55,66,89])
print(set_example)
print(len(set_example))

#min(), max()
number = [7,8,99,60,898,1000]
print(number)
print(min(number))
print(max(number))

#count()
number = [2,2,2,4,5,6,7,8,9,9,9]
print(number)
print(number.count(2))

#substring()
string = "njoel the great"
substring = "e"
print(string.count(substring))

#in(), not in()
sentence = "Matematika itu mudah dan menyenangkan bukan ?"
print('Fisika' not in sentence)
print('Fisika' in sentence)

#value in multiple variable
data = ['shirt', 'whiite', 'L']
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

#sort()
alphabet = ['b', 'c', 'e', 'd', 'a']
print(alphabet)
alphabet.sort()
print(alphabet)
alphabet.sort(reverse=True)
print(alphabet)
#operation list, set and string -------------->
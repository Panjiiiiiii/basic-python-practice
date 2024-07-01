#if/else
avalaible = 2

if avalaible < 20 :
    print("Stok tidak cukup")
elif avalaible == 20 :
    print("Stok cukup")
else : 
    print("Stok melimpah")

#ternary operators
laku = False
print("Produk habis") if laku else print("Produk masih banyak")

#ternary operators (tuples)
laku = True
stok = ("Stock masih banyak","Stock habis")[laku]
print(stok)

#looping
var_list = [1,2,3,4,5]
print("Looping for")
for i in var_list:
    print(i)

#looping range()
print("Looping range")
for i in range(1,10,3):
    print(i)

#looping while
counter = 1
print("Looping while")
while counter <= 5 :
    print(counter)
    counter +=1

#nested for()
print("Nested for()")
for i in range (1,3) :
    for j in range (1,3) :
        print(i,j)


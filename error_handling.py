#try exception
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Can't divide with 0")

#except statement
var_dict = {"Total": "10"}
try:
    print(f"Total is {var_dict['Total']}")
except KeyError:
    print("Key not found")
except TypeError:
    print("Can't divide value with string")
else :
    print("Code executed without exception")
finally :
    print("Code success")
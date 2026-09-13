# ============================================================
# Lab 1 - Introduction to AI and Its Application Using Python
# ============================================================

print("Hello, World!")

# ------------------------------------------------------------
# Comments in Python
# ------------------------------------------------------------

x = 1
# The initial value of x is 1.
if x > 0:
    print("These are two comments")  # Print a string.

# ------------------------------------------------------------
# Input / Output
# ------------------------------------------------------------

# Concept: input() takes user input/ print() displays output.
txt = input("Type something to test this out: ")
print(txt)

# ------------------------------------------------------------
# Multiple Statements on a Single Line
# ------------------------------------------------------------

# Concept: Two statements can be written on a single line using a semicolon (;).
print("Statement1")
print("Statement2")

# You can write above two statements in the following way
print("Statement1"); print("Statement2")

# ------------------------------------------------------------
# Indentation
# ------------------------------------------------------------

x = 1
if x > 0:
    print("This statement has a single space Indentation")
    print("This statement has a single space Indentation")

if x > 0:
    print("This statement has a single tab Indentation")
    print("This statement has a single tab Indentation")

# ------------------------------------------------------------
# Data Types and Type Casting
# ------------------------------------------------------------

a = 1452
print(type(a))      # <class 'int'>

b = -4587
print(type(b))      # <class 'int'>

c = 0
print(type(c))      # <class 'int'>

g = 1.03
print(type(g))      # <class 'float'>

h = -11.23
print(type(h))      # <class 'float'>

i = .34
print(type(i))      # <class 'float'>

j = 2.12e-10
print(type(j))      # <class 'float'>

k = 5E220
print(type(k))      # <class 'float'>


x = complex(1, 2)
print(type(x))      # <class 'complex'>
print(x)            # (1+2j)

z = 1 + 2j
print(type(z))      # <class 'complex'>

z = 1 + 2J
print(type(z))      # <class 'complex'>


x = True
print(type(x))      # <class 'bool'>

y = False
print(type(y))      # <class 'bool'>


str1 = "String"  
print(str1)

str2 = 'String'  

str2 = "Day's"      
print(str2)

str2 = 'Day"s'      
print(str2)


# ---------------- Special Characters in Strings ----------------
print("This is a backslash (\\) mark.")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")

# ---------------- String Indices and Accessing String Elements ----------------

string1 = "PYTHON TUTORIAL"
print(string1[0])     
print(string1[-15])   
print(string1[14])    
print(string1[-1])    
print(string1[4])     
print(string1[-11])  
# print(string1[16])  Error


print(string1[3:7])


# ------------------------------------------------------------
# Lists
# ------------------------------------------------------------


my_list1 = [5, 12, 13, 14]              # the list contains all integer values
print(my_list1)

my_list2 = ['red', 'blue', 'black', 'white']  # the list contains all string values
print(my_list2)

my_list3 = ['red', 12, 112.12]          # the list contains a string, an integer and a float
print(my_list3)


my_list = []
print(my_list) #Empty


color_list = ["RED", "Blue", "Green", "Black"]  # the list has four elements, indices start at 0 and end at 3
print(color_list[0])               
print(color_list[0], color_list[3])
print(color_list[-1])              
# print(color_list[4])   #error


print(color_list[0:2])  
print(color_list[1:2])   
print(color_list[1:-2])  
print(color_list[:3])     
print(color_list[:])      

# ------------------------------------------------------------
# Conditional Statements
# ------------------------------------------------------------

a = 5
b = 10
if b > a:
    print("b is greater than a")

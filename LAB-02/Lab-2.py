
# While Loop

# x=0
# while x<10:
#     print(x)
#     x=x+1





# count =0
# while count == 0:
#     print("Hello")

    # infinte loop becomes


# for in loop

# I= ['greeks','for','geeks']
# J= ('greeks','for','geeks')

# for i in I:
#     print(i)

# print("Tuple iterations")
# for j in J:
#     print(j)


#iterating over a string

# c="Geeks"

# for i in c: 
#     print(i)

#with the help of length

# I= ['greeks','for','geeks']
# for i in range(len(I)):
#     print(I[i])

#Loop Control Statements

# 1. Continue 

# a= 'geeksforgeeks'

# for i in a:
#     if i=='e' or i=='s':
#         continue
#     print(i)


# 2. Break
# a= 'geeksforgeeks'

# for i in a:
#     if i=='e' or i=='s':
#         break
#     print(i)


# Creating a Function

# def my_function():
#     print("Hello from a function")

# my_function()


#with the help of parameters


# def my_function(fname):
#     print(fname + " Refnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


    #passing default value as parameter

# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()   
# my_function("Brazil")


# Passing a List as a Parameter

# def my_function(food): 
#     for x in food: 
#         print(x) 

# fruits = ["apple","banana","cherry"] 
# my_function(fruits)

    # return function

# def my_function(x):
#     return 5 * x    

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# def my_function(child3,child2,child1): 
#     print("The youngest child is " + child3) 

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


###############################################################################

                   # OOPS

#################################################################################


# class MyClass:
#   x = 5

# o1 = MyClass()
# print(o1.x)


# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

p1= Person("John", 36)
p1.myfunc()
  



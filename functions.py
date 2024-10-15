# def greet():
#     return "Today I am learning function"

# for i in range(5):
#     print(greet())

# def add_2(n1:int,n2:int) ->int:
#     total = n1+n2
#     return total

# def check_num(num:int)-> str:
#     if num %2 == 0:
#         return ("even")
#     else:
#         return ("odd")


# x=  int(input("enter the num1 : "))
# y = int(input("enter the num2 : "))

# num = add_2(x,y)
# print(num)

# print(check_num(num))

""" 
Types Of parameter:
1.positional Argument
2.*args - this retirn as a tuple
3.**Kwargs - this return a dictionary
4.default
"""


# def hiddenfunction(*args):
#     print(args)

# hiddenfunction(1,2,3,4,5,6,7)

# def fool(a,b,*args,**kwargs):
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key,kwargs[key])

# enforce argument: any argument after * or *args is considered as keyword argument

# def fool(a,b,*,c,d):
    # print(a,b,c,d)

# fool(1,2,c = 7,d = 8)
# Note : The lenght of list and dictionary must be equal to no of parameters passed in the functions
# def foo(a,b,c):
#     print(a,b,c)


# my_dict = {"a":1,"b":2,"c":3}
# foo(**my_dict)

# lambda is an anonymous function it takes multiple parameters and the operation which we want to perfoem and store it in a variable.

# result = lambda n : [ i for i in range(1,10)]
# print(result(6))

# Annotation
def add_two(x:int,y:int):
    total = x+y
    return total

# print(add_two(10,20))







# name = "Mukesh"
# print("Hi, there! my, name, is",name, sep = "|")

# strings = ["hello","Mukesh","Rahul","Manoj","Rohit","There"]

# lengths = map(len,strings)

# print(list(lengths))


# def add_s(strings : list):
#     strings1 = []
#     for i in strings:
#         strings1.append(i + "s")
#     print(strings1)

# strings = ["hello","Mukesh","Rahul","Manoj","Rohit","There"]

# add_s(strings)

# def add_s(strings):
#     return strings+ "s"
# strings = ["hello","Mukesh","Rahul","Manoj","Rohit","There"]


# lst = map(add_s,strings)
# print(list(lst))

# def add_s(strings):
#     return len(strings)>4

# strings = ["hel","Mesh","Rahul","Manoj","Rohit","There"]

# filtered = filter(add_s,strings)
# print(list(filtered))

def sum_list(x:list[int]):
    result = 0
    for i in x:
        result+=i

    return result

print(sum_list([1,2,3,4,5,6,7]))




class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
blu.name = "aditya"
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
#Encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()
#you can't modify value
c.__maxprice = 45346
# using setter function
c.setMaxPrice(1000)
c.sell()
#Polymorphism
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

# c1 = ComplexNumber(2,3)
# del c1.imag
# c1.getData()
# Traceback (most recent call last):
# ...
# AttributeError: 'ComplexNumber' object has no attribute 'imag'

# >>> del ComplexNumber.getData
# >>> c1.getData()
# Traceback (most recent call last):
# ...
# AttributeError: 'Comp

class test():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return ("sum = {}".format(self.a+self.b))

t = test(10,20)
print (t)

#generator
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        print (i)
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)

test = lambda x : x * x

print (test(3))


# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)

# Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
# next(a)

sum(x**2 for x in my_list)
# 146

max(x**2 for x in my_list)
# 100
#generator
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))


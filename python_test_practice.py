# create a function called user_name
def user_name():
    pass

# how would you iterate over the following list: arr = [1,2,3,4,5]?
# display the list with help of for loops and a print statement
def iterator(lst):
    for item in lst:
        print(item)

# && AND || andand : which one is the correct boolean value/operator?

# and

# what is the difference between tuple and a list?

# tuples are immutable, they cannot be modified, a list is mutable it can be modified (added to, removed from, values alter/replaced)

# could you add an element in a tuple?

# no

# can you have multiple types of data in a tuple?

# yes

# data_type = {'0' : 0, '1' : 1, '2' : 2} what type of data collection is this?

# a mixed dictionary - dict

# how to create an object of a class called DevOps()

# new_object = DevOps()

# adds 5 to the following list?
arr = [1,2,3,4]
arr.append(5)


# using a function that takes 1 arg, return True if arg is equal to DevOps, otherwise False

def DevOps_Checker(item):
    return (True if item.upper() == "DEVOPS" else False)

# how to inherit a class - write the correct syntax if you had class Y and class Z - inherit class Z from class Y

# from z import Z
# class Y(Z):

# how to declare super

# super().__init__()

# a function should return True if value is contained [list] at an even index, False otherwise

def list_checker(lst, desired):
    for item in lst:
        if item == desired:
            return True
    return False

# create 4 functions that take 2  args each, percentage(value1, value2), divide, calculate DoB, multiply
# in each function check to ensure the value entered is not 0
# each function must return correct mathematical value

def percentage(val1, val2):
    return str((val1/val2)*100)+"%"

def divide(val1, val2):
    return val1/val2

def multiply(val1,val2):
    return val1*val2

def calc_DoB(year, age):
    return year - age

# searching odd and even numbers using a function that an argument of ints
# using range ()

def odd_or_even(numbers):
    odd_even = [0, 0]
    for this in numbers.range():
        if (this%2) == 0:
            odd_even[0] += this
        else:
            odd_even[1] += this
    return odd_even

# create a function to calculate total value of shopping bill
# shopping_lsit = {5 items with values  3.4, 5.5, 6, 7 in a key value format}
# must return the total amount only

def shopping_list_bill(shopping_list):
    total = 0
    for item in shopping_list.values():
        total += item
    return total
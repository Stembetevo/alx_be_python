def greet(name):
    print("Good Afternoon:",name)
greet("Steve")

def calulate_area(length,width):
    area = length * width
    return area
print(calulate_area(20,30))

def is_even(num):
    if(num%2 == 0):
        print("Number is even")
    else:
        print("Number is odd")
is_even(46)
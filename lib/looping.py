#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    updated_list = list()
    for int in int_list: 
        updated_list.append(int**2)
        # print(updated_list)
    return updated_list
    
    
    pass

def fizzbuzz():
    # code goes here!

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
    pass

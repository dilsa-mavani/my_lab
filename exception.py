try:
    number1=int(input("enter a number:"))
    number2=int(input("enter another number:"))
    result=number1/number2

except ZeroDivisionError:
    print("you cannot divide by zero!")
except valueError:
    print("please enter a valid number!")
else:
    print("Division successfull Result is:",result)
finally:
    print("This block always runs.")  



try:
    my_list=[1, 2, 3]
    print(my_list[1])
except indexError:
    print("index is out of range!")
else:
    print("Element found successfully!")
finally:
    print("program finished.")                                  
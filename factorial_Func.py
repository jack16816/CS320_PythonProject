
def factorial_Func():
    num = input("Of what number do you want to know the factorial? ")   #Prompt for Factorial number calculation

    facto_result = 1
    for x in range(1,num+1):                                            #Loop that calucates factorial of given number
        facto_result = x * facto_result

    print("The factorial of {} is {}." .format(num, facto_result))      #Print Result
    print("")
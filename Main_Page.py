
from factorial_Func import factorial_Func


print("Welcome to the function chooser, please select what number function you would like: ")       #Welcome Statement
print("Factorial Calucltor ........... 1")                                                          #Factorial Function

choice = input("Your choice is: ")                                                                  #Prompt for function choice

if choice == 1:                         #Run Factorial function is it is chosen
    factorial_Func()


print("That was fun!")                  #Ending Statement

    
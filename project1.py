'''
Project 1 - Happy Numbers - Fall 2025  
Author: Lamiek Haile 

This program takes a value
I have neither given or received unauthorized assistance on this assignment.
Signed:  Lamiek Haile
'''



def sum_of_squares(n):
    ''' This function takes an inputted value and gets the remainder after dividing by 10.
Then with that number they square it and keep looping until they get the total sum of squares
'''
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10
    return total
        
def is_happy(n):
    '''This takes the n from the previous function and checks if it is a happy number.
First however, it checks if its not 1 or 42,if it isn't, it will keep going through the sum of squares function.
If it keeps looping it will be set to False
However, if it is it will set it to True
'''
    while n != 1 and n != 42:
        n = sum_of_squares(n)
        print()
        print(n)
        
    if n == 1:
        return True
    if n == 42:
        return False
    
def main():
    '''This is the introductory stuff, so where the intro statement is placed,
where the inputing goes, how the values stay positive and, where you quit by pressing 0, and finally where the outcome is printed
'''

    print("Welcome! I'll check if your numbers are happy or not happy.")
    print()
   
    while True:
        print()
        enter = int(input("Please enter any positive integer (or 0 to quit)): "))

        while enter < 0:
            enter = int(input("The number must be positive. Please reenter (or 0 to quit): "))

        if enter == 0:
            print()
            print("Have a happy day!")
            break

        if is_happy(enter) == True:
            print(f'{enter} is a happy number!')
        else:
            print(f'{enter} is NOT a happy number.')

    

    
if __name__ == '__main__':
    main()








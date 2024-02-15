#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# To submit this assignment in D2l, post the link to your notebook file on your GitHub account.

# ## 4.1 Even or Odd Checker
# Create a program that checks whether a number is even or odd.
# 
# ### Console:
# ```powershell
# Even or Odd Checker
# 
# Enter an integer: 33
# This is an odd number.
# ```
# 
# ### Specifications:
# - Store the code that gets user input and displays output in the main function.
# - Store the code that checks whether the number is even or odd in a separate function.
# - Assume that the user will enter a valid integer.
# 

# In[38]:


### CODE HERE ###
print()
print("Even or Odd")
print()
def oddOrEven(num):
    even = num % 2
    if even == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

def main():
    userInp = int(input("Enter an interger: "))
    oddOrEven(userInp)
    
if __name__ == "__main__":
    main()


# ## 4.2 - Feet and Meters Converter
# Create a program that converts feet to meters and vice versa.
# 
# ### Console
# ```powershell
# Feet and Meters Converter
# 
# Conversions Menu:
# a.	Feet to Meters
# b.	Meters to Feet
# Select a conversion (a/b): a
# 
# Enter feet: 100
# 30.48 meters
# 
# Would you like to perform another conversion? (y/n): y 
# 
# Conversions Menu:
# a.	Feet to Meters
# b.	Meters to Feet
# Select a conversion (a/b): b
# 
# Enter meters: 100
# 328.08 feet
# 
# Would you like to perform another conversion? (y/n): n
# 
# Thanks, bye!
# ```
# 
# ### Specifications:
# - The formula for converting feet to meters is:
# `feet = meters / 0.3048`
# 
# - The formula for converting meters to feet is:
# `meters = feet * 0.3048`
# 
# - Store the code that performs the conversions in functions within a module. For example, store the code that converts feet to meters in a function in a module.
# - Store the code that displays the title in its own function, and store the code that displays the menu in its own function, but store the rest of the code that gets input and displays output in a main function.
# - Assume the user will enter valid data.
# - The program should round results to a maximum of two decimal places.
# 
# 
# 

# In[2]:


### CODE HERE ###
print()
print("Feet and Meters Converter")
print()
print("Conversions Menu:")
print("a. Feet to Meters")
print("b. Meters to Feet")
userInp = input("Select a conversion (a/b): ")


# ## 4.3 - Sales Tax Calculator
# Create a program that uses a separate module to calculate sales tax and total after tax.
# 
# ### Console
# ```powershell
# Sales Tax Calculator
# 
# ENTER ITEMS (ENTER 0 TO END)
# Cost of item: 35.99 
# Cost of item: 27.50 
# Cost of item: 19.59 
# Cost of item: 0 
# Total:  83.08
# Sales tax:	4.98
# Total after tax: 88.06 
# 
# Again? (y/n): y
# 
# ENTER ITEMS (ENTER 0 TO END)
# Cost of item: 152.50 
# Cost of item: 59.80 
# Cost of item: 0
# Total:  212.3
# Sales tax:	12.74
# Total after tax: 225.04 
# 
# Again? (y/n): n
# 
# Thanks, bye!
# 
# ```
# 
# ### Specifications
# - The sales tax rate should be 6% of the total.
# - Store the sales tax rate in a module. This module should also contain functions that calculate the sales tax and the total after tax. These functions should round the results to a maximum of two decimal places. Upload the seperate sales tax module to your GitHub repo when submitting.
# - Store the code that gets input and displays output in this notebook. Divide this code into functions wherever you think it would make that code easier to read and maintain.
# - Assume the user will enter valid data.
# 
# 

# In[3]:


### CODE HERE ###


# ## 4.4 - Prime Number Checker
# Create a program that checks whether a number is a prime number and displays the total number of factors if it is not a prime number.
# 
# ### Console
# ```powershell
# Prime Number Checker
# 
# Please enter an integer between 1 and 5000: 1 
# Invalid integer. Please try again.
# Please enter an integer between 1 and 5000: 2
# 2 is a prime number. 
# 
# Try again? (y/n): y
# 
# Please enter an integer between 1 and 5000: 3
# 3 is a prime number.
# 
# Try again? (y/n): y
# 
# Please enter an integer between 1 and 5000: 4
# 4 is NOT a prime number.
# It has 3 factors.
# 
# Try again? (y/n): y
# 
# Please enter an integer between 1 and 5000: 6
# 6 is NOT a prime number.
# It has 4 factors.
# 
# Try again? (y/n): n
# 
# Bye!
# ```
# 
# ### Specifications
# - A prime number is only divisible by two factors (1 and itself). For example, 7 is a prime number because it is only divisible by 1 and 7.
# - If the number is not a prime number, the program should display its number of factors. For example, 6 has four factors (1, 2, 3, and 6).
# - Store the code that gets a valid integer for this program in its own function.
# - Store the code that calculates the number of factors for a number in its own function.
# - Store the rest of the code that gets input and displays output in the main function.
# 
# 

# In[ ]:


### CODE HERE ###


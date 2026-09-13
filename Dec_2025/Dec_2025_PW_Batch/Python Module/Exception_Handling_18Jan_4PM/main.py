# user-defined module
import calculator as calc
import string_utils as st

num = 5
fact_result = calc.factorial(num)
square_result = calc.square(num)
cube_result = calc.cube(num)

print(f"Factorial of a given number {num} is {fact_result}")
print(f"Square of a given number {num} is {square_result}")
print(f"Cube of a given number {num} is {cube_result}")


string1 = 'priya'
string2 = 'bhatia'
reverse_str = st.reverse_string(string1)
palindromic_check = st.palindrome_string(string1)
concatenation_str = st.concatenate_string(string1, string2)

print(f"The reverse of a given string {string1} is {reverse_str}")
print(f"The palindrome check of a given string {string1} is {palindromic_check}")
print(f"The concatenation of a {string1} and {string2} is {concatenation_str}")
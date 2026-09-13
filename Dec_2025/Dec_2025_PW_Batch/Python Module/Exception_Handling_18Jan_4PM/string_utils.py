'''
 This file operates as a module which contains all the required 
 functions of string
'''

def reverse_string(s):
    '''This function returns the reverse of the given string'''
    return s[::-1]

def palindrome_string(s):
    '''This function returns whether the string is palindromic or not'''
    return s == s[::-1]

def concatenate_string(s1, s2):
    '''This function returns the string concatenation'''
    return s1 + s2

def string_length(s):
    '''This function returns the length of the given string'''
    return len(s)
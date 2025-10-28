# string methods 

# 1) Lower case ( lower ()) : It converts a string into lower case 

x = "pyTHOn"
print(x.lower())

# 2) Upper case ( upper() ) : It converts a string into upper case 

x = "pyTHOn"
print(x.upper())

# 3) Capitalize ( capitalize() ) : It converts the first character of each word into upper case 

x = "i am a student"
print(x.capitalize())

# 4) Title ( title () ) : It converts the first character of each word into upper case 

x = "i am a student"
print(x.title())

# 5) Swapcase ( swapcase () ) : It swaps the cases, lower case becomes upper case and vice-versa 

x = "pyTHOn"
print(x.swapcase())

# 6) Checking lower case ( islower () ) : It returns 'True' if all characters in the string are lower case 

x = "python"
print(x.islower())    # True

x = "PyTHon"
print(x.islower())    # False

# 7) Checking upper case ( isupper () ) : It returns true if all characters in the string are upper case 

x = "PYTHON"
print(x.isupper())    # True

x = "PYThon"
print(x.isupper())

# 8) Checking Title ( istitle () ) : It returns True if the string follows the rules of a title

x = "Python String Method"
print(x.istitle())           # True

x = "python String methods"
print(x.istitle())           # False 

# 9) Checking Numbers ( isdigit() ) : It returns True if all characters in the string are digits

x = "123"
print(x.isdigit())     # True

x = "123abc" 
print(x.isdigit())     # False

# 10) Checking alphabets ( isalpha () ) : It returns True if all characters in string are alphabets 

x = "abc"
print(x.isalpha())     # True

x = "abc123"
print(x.isalpha())     # False

# 11) Checking Alphanumeric Characters ( isalnum () ) : It returns True if all the characters in the string are alpha-numeric 

x = 'abc123'
print(x.isalnum())     # True

x = 'abc123@#$'
print(x.isalnum())     # False

# 12) a ) strip() : Returns a trimmed version of a string 

x = "-----Python-----"
print(x.strip("-"))         # Python

x = "-----Python-----"
print(x.lstrip("-"))        # Python-----

x = "-----Python-----"
print(x.rstrip("-"))        # -----Python   


# 13) Checking the start value of string ( startswith () ) : It returns True if the string starts with the specified value 

x = 'python'
print(x.startswith("p"))    # True

x = "Python"
print(x.startswith("p"))    # False 

# 14) Checking the Endvalue of string ( endswith() ) : It returns True if the string ends with a specified value

x = "Python"
print(x.endswith('n'))      # True

x = "python"
print(x.endswith('N'))      # False 

# 15) Count ( count () ) : It returns the number of times a specified value occurs in a string 

x = "python string methods"
print(x.count('t'))         # 3
print(x.count('s'))         # 2 

# 16) Index ( index() ) : It searches the string for a specified value and returns the position of where it was found 

x = 'python'
print(x.index('t'))

# 17) Replace ( replace() ) : It returns a string where a specified value is replaced with a specified value

x = 'Python string methods'
x = x.replace('s','S')
x = x.replace('m', "M")
print(x)                    # Python String Methods



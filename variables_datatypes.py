# simple combination of strings 
# usage of variables with strings then combine

cig = 'iqos'
yos = 'marlboro'

print(cig, 'is better than', yos, 'prove me WRONG!')


#newline \n
print('Giraffe\nAcademy')

#\' hey Python we want to print a quotation mark
print('Giraffe\'Academy')

#.lower() = convert string to lower case
mura = 'Putangina Mo'
print(mura.lower())
# .upper() = convert string to upper case
mura = 'Putangina Mo'
print(mura.upper())
#to check if string is lower or upper = returns a Bool
mura = 'Putangina Mo'
print(mura.isupper())
#convert to upper case then check if uppercase
mura = 'Putangina Mo'
print(mura.upper().isupper())

print('=====================')

#checking length of string
mura = 'Putangina Mo'
print(len(mura))
#grabbing individual characters in a string (indexing)
mura = 'Putangina Mo'
print(mura[0])
#index function (where is placement of character string)
mura = 'Putangina Mo'
print(mura.index('Mo'))
#replace function (2 values) (first value what to relace, 2nd what to replace with)
mura = 'Putangina Mo'
print(mura.replace('Putangina', 'Tangina'))
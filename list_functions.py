# extend = appending to a list
lucky_numbers = [1, 2, 3, 4, 5, 6]
friends = ['Karl', 'Karen', 'Jim', 'Oscar', 'Tamia']
#friends.extend(lucky_numbers)

# adding individual elements to list via append
friends.append('Gago')
print(friends)
# adding an individual element to a specific index of a list via insert pushing other elements like a wisdom tooth
friends.insert(1, 'Tangina')
print(friends)
print('===========')
# removal of friends via remove 
friends.remove('Jim')
print(friends)
# resetting the list via clear
#friends.clear()
#print(friends)

print('==============')
# pop == removes the last element inside the list
friends.pop()
print(friends)

# index asking python where is the position of our element == also good for looking up if a specific element is in our array
print(friends.index('Oscar'))

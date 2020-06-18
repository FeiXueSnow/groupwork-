ORIGINAL = ['M', 'A', 'R', 'S', 'T', 'V']

# print the original list
print('Original list is', ORIGINAL)

# print an emtpy line
print('\n')

# make a copy of the original list
team = ORIGINAL[0:5]

# 1. change individual element: change the last element to 'X'
team[5] = "X"
print(f'1:\t\t{team}')

# 2. add a new element 'Z' at the end of list
  # add your answer at the beginning of this line
team.append(z)
print(f'2:\t\t{team}')

# 3. add a new element 'B' at the 2nd position (index 1)
team.insert(1, "B")
print(f'3:\t\t{team}')

# 4. remove the third element (index 2) in the list: two ways
# 4.1 by index 2
del team[2]
print(f'4.1:\t{team}')
# 4.2 by value 'R'
team.remove("R")
print(f'4.2:\t{team}')

# 5. pop an element from the list
# 5.1 pop the last element and print it out, in one line of code
print(team.pop())
print(f'5.1:\t{team}')

# 6. get the length of the list
print(f'6:\t\t{team} has', len(team), 'items')

# 7. sort the list
# 7.1 sort the list alphabetically
  # add your answer at the beginning of this line
print(f'7.1:\t{team}')
# 7.2 sort the list in reverse alphabetical order
  # add your answer at the beginning of this line
print(f'7.2:\t{team}')

# reset list
team = ORIGINAL[:]

# 8. reverse the order of the list
  # add your answer at the beginning of this line
print(f'8:\t\t{team}')

# 9. print all items in the list, one item in each line
print('9:')
# add your answer in next two lines



# end
print('\nOur group is fantastic!')

#open file
f = open('data.txt')

#use file
print('Name: ', f.name)
print('close: ', f.closed)
print('access mode: ', f.mode)

#close file
f.close()

print('\nAfter Close')
print('Closed: ', f.closed)
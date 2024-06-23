#open file
f = open('data.txt', 'r')

#write data in file
s = f.read()

print('data: ')
print(s)

f.close()
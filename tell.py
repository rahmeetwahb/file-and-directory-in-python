#open file
f = open('data.txt', 'r')

print('before the file is read')
print('position file: %d' % f.tell())

#reading data of 15byte
data1 = f.read(15)

print('after reading file of 15 byte')
print('data1: %s' % data1)
print('position file: %d' % f.tell())

#read again data of 5
data2 = f.read(5)

print('after reading file of 5 byte')
print('data2: %s' % data2)
print('position file: %d' % f.tell())
import os

#get information about active directory
s = os.getcwd()
print('active directory: ', s)

#change directory
os.chdir('F:\\learn\\program\\python\\file and directory\\directory1')

print('after change directory')
print('active directory: ', s)
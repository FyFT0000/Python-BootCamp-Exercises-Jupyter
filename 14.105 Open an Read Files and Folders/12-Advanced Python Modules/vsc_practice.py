import os


f = open('vsc_practice.txt','w+')
f.write('This is a test string in VSC')
f.close()
print('')
print(os.getcwd())
print('')
print(os.listdir(os.getcwd()))
print('')
print('End of Execution')
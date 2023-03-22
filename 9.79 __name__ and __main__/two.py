#two.py

import one
print('Top leven in two.py')

one.func()

if __name__ == '__main__':
    print('two.py is being run directly')
else:
    print('two.py has been imported')
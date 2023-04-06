
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

stmt_one = '''
func_one(100)
'''
setup_one = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt_two = '''
func_one(100)
'''
setup_two = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''


print(f'func_one time: {timeit.timeit(stmt_one,setup_one,number=500000):9}')
print(f'func_two time: {timeit.timeit(stmt_two,setup_two,number=500000):9}')

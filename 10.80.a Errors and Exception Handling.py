try:
    f = open('testfile1.txt','r')
    f.write("Write a test line1")
except TypeError:
    print('There was a Type error')
except OSError:
    print('Hey you have an OS error')
except:
    print('All other exceptions!')
finally:
    print('I always run')

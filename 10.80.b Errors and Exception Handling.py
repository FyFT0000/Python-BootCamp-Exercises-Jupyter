#from IPython.display import clear_output
import os
#clear = lambda: os.system('clear')
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            #print('\n'*10)
            #clear_output()
            #clear()
            cls()
            print("Whoops that is not a number")
        else:
            print("Yes Thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I'm going to ask you egain!\n")



ask_for_int()

# import only system from os
from os import system, name
import random
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()
print('   THE HANGMAN GAME')
print('_______________________\n')
List = ['cat','dog','horse','rhino','tiger']
k = random.randint(0,len(List)-1)
string = '-'*len(List[k])
t=0
def h(x):
    if x==1:
        #1
        print('---------')
        print('    |    ')
        print('         ')
        print('         ')
        print('         ')
        print('         ')
    elif x ==2:
        #2
        print('---------')
        print('    |    ')
        print('         ')
        print('         ')
        print('         ')
        print('   /     ')
    elif x ==3:
        #3
        print('---------')
        print('    |    ')
        print('         ')
        print('         ')
        print('         ')
        print('   / \   ')
    elif x==4:
        #4
        print('---------')
        print('    |    ')
        print('         ')
        print('         ')
        print('    |    ')
        print('   / \   ')
    elif x==5:
        #5
        print('---------')
        print('    |    ')
        print('         ')
        print('     \   ')
        print('    |    ')
        print('   / \   ')
    elif x==6:
        #6
        print('---------')
        print('    |    ')
        print('         ')
        print('   / \   ')
        print('    |    ')
        print('   / \   ')
    elif x == 7:
        #7
        print('---------')
        print('    |    ')
        print('         ')
        print('   /|\   ')
        print('    |    ')
        print('   / \   ')
    elif x==8:
        #8
        print('---------')
        print('    |    ')
        print('    O    ')
        print('   /|\   ')
        print('    |    ')
        print('   / \   ')



m = 1


while t!=8 and m<=len(string):
    print("guess the animal:",string)
    i = input()
    clear()
    
    if i in List[k]:
        print('   THE HANGMAN GAME')
        print('________________________\n')
        h(t)
        index = List[k].index(i)
        string = string[:index] + i + string[index+1:]
        m += 1
    else:
        t += 1
        print('   THE HANGMAN GAME')
        print('________________________\n')
        if t<=7:
            h(t)
        else:
            print("You are hanged!")
            h(t)
    if m==len(string)+1:
        print("You survived!")  
            





        







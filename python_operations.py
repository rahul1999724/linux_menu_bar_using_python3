from os import system as sys
from termcolor import colored

print(colored("""
Enter 1 :launch python

Enter 2 :Run your python file
Enter 3 :Install a package
Enter 4 : To exit from python operations""","green"))

while True:
        x = int(input("Enter no. of your choice (for python) : "))
        if x == 1:
                sys('python3')

        elif x == 2 :
                pth = input("Enter name of the file you want to run : ")
                sys("python3 {}".format(pth))
        elif x == 3 :
                nm = input ("Enter package name : ")
                sys("pip3 install {}".format(nm))
        elif x == 4 :
                sys("exit")
                break
        else :
                print(colored("Invalid input !!!","red"))

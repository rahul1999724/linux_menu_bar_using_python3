import os
from os import system as sys
import getpass
from termcolor import colored

#code for banner and design
print(sys("figlet ARTH 2020"))
print()


print("\t\t\t Welcome to my menu")

#read password from file
f = open("password.txt",'r')
password = f.readline()


#password setup
#x = getpass.getpass("Enter Your Password : ")
#if x == password:
#    print(colored("Login Successful !" , "green"))
#    print()
#else:
#    print(colored("Password is Incorrect !" , "red"))


print("\t\t\t---------------------")

#menu-program-fea
while True:


        print(colored("""Enter 1  : For Linux Operations
Enter 2  : For Python Operations
Enter 3  : For Docker Operations
Enter 4  : For AWS Operations
Enter 5  : For Hadoop Operations

Enter 6  : To Exit from Main Program
        ""","blue"))

        ch = input("Enter your choice (main menu): ")
        print(ch)

        if int(ch) == 1:
            sys("python3 linux_operations.py")
        if int(ch) == 2:
            sys("python3 python_operations.py")

        elif int(ch) == 3:
            sys("python3 docker_operations.py")

        elif int(ch) == 4:
            sys("python3 aws_operations.py")

        elif int(ch) == 5:
            sys("python3 hadoop_operations.py")

        elif int(ch) == 6:
            sys("exit")
            break

        else:
            print(colored("not supported","red"))



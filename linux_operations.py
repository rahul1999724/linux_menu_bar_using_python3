from os import system as sys
from termcolor import colored
import getpass
import smtplib

print(colored("""Enter 1  : to login as root user
Enter 2  : to see date & time
Enter 3  : to open calculator
Enter 4  : to create new user
Enter 5  : to install new software or tool
Enter 6  : to open new terminal
Enter 7  : to open text-editor
Enter 8  : to update whole system
Enter 9  : to scan website using nmap
Enter 10 : to check ip address
Enter 11 : to ping
Enter 12 : to configure web server
Enter 13 : to run any command
Enter 14 : to launch browser
Enter 15 : to search location of installed software/tool
Enter 16 : to open website
Enter 17 : to send an email
Enter 18 : to exit from linux operations
        ""","yellow"))



while True:
    ch = int(input("Enter the no. of your choices (linux op) : "))

    if(ch == 1):
        sys("sudo su")
        print()

    elif(ch == 2):
        sys("date")
        print()
        
     elif(ch == 3):
        sys("bc")
        print()

    elif(ch == 4):
        print("Enter user name : ",end="")
        create_user = input()
        sys("useradd {}".format(create_user))
        print()

    elif(ch == 5):
        print("Enter software name: ",end="")
        software_name = input()
        sys("sudo yum install {}".format(software_name))

    elif(ch == 6):
        sys("gnome-terminal")
        print()

    elif(ch == 7):
        sys("vim new.txt")
        print()

    elif(ch == 8):
        sys("sudo yum update")
        print()


    elif(ch == 18):
        sys("exit")
        break

    else:
        print(colored("Invalid Choice","red"))
                                        

                                                                          1,29          Top

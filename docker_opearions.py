from os import system as sys
from termcolor import colored

print(colored("""
Enter 1 : to install docker
Enter 2 : to see docker information
Enter 3 : to start docker services
Enter 4 : to see docker status
Enter 5 : to see images
Enter 6 : to launch container
Enter 7 : to see running containers
Enter 8 : to stop container
Enter 9 : to pull image from docker hub
Enter 10 : to see network list
Enter 11 : to go inside container
Enter 12 : to delete image permanently
Enter 13 : to exit from docker operations
""","yellow"))

while True:
    x = int(input("Enter no. of your choices (for docker) : "))

    if x == 1: #install docker
        sys("sudo yum install docker-ce --nobest")

    elif x == 2: #to check docker information
        sys("sudo docker info")

    elif x == 3: # to start docker service
        sys("sudo systemctl start docker")

    elif x == 4: # to see docker status
        sys("systemctl status docker")

    elif x == 5: # to see images
        sys("sudo docker images")
        print()
        
     elif x == 6: # to launch conatiner
        os_name = input("Enter your os_name : ")
        image_name = input("Enter your image_name : ")
        sys("sudo docker run -dit --name {} {}".format(os_name,image_name))
        print()


    elif x == 7: # to see running containers
        sys("sudo docker ps -a")
        print()

    elif x == 8: # to stop containers
        os_name = input("Enter os_name u want to stop : ")
        sys("sudo docker stop {}".format(os_name))
        print()

    elif x == 9: # to pull image from docker hub
        image_name = input("Enter image_name : ")
        tag = input("Enter your tag_name : ")
        sys("sudo docker pull {}:{}".format(image_name,tag))
        print()


    elif x == 10: #to see network list
        sys("sudo docker network ls")
        print()

    elif x == 11: # to go inside container
        os_name = input("Enter os_Name : ")
        sys("sudo docker exec -it {} bash".format(os-name))
        print()

    elif x == 12: # to delete docker image
        doc_ima = input("Enter Image name to delete")
        sys("sudo docker rmi {}".format(doc_ima))
        print()
        
        
     elif x == 13:
        sys("exit")
        break

    else:
        print(colored("Invalid input !!!!", "red"))

              

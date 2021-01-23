import os
from termcolor import colored

print (colored("""
Press 1  : to create a Key Pair .
Press 2  : to see details of instances ...
Press 3  : to create an EBS Volume .
Press 4  : to create a instance .
Press 5  : to create a S3 bucket.
Press 6  : to delete a S3 bucket.
Press 7  : to delete key pair.
Press 8  : to launch a instance with configured Web server
Press 9  : to start a instance.
Press 10 : to stop a instance .
Press 11 : to terminate a instance .
Press 12 : to create a cloudfront distribution .
Press 13 : to attach the extra volume .
Press 14 : to exit from aws operations .
""","red"))

while True:
    x = int(input("Enter No. of your choice (for aws) : "))


    if x == 1: #to create key-pair
        key_name = input("Enter key_name : ")
        os.system("aws ec2 create-key-pair  --kay-name {}".format(key_name))
        print("Task completed ....")

    elif x == 2: # to see instances  details
        os.system("aws ec2 describe-instances")
        print("Task completed ....")


    elif x == 3: #to create an ebs volume
        size = int(input("Enter the size you want"))
        az = input("Enter the zone where you want to create ebs volume to be deployed : ")
        type = input("Enter the volume type u want : ")
         os.system("aws ec2 create-volume availability-zone {} --size {} --volume-type {}".format(az,size,type))


    elif x == 4: # to create an instance
        image_id = input("Enter image_id : ")
        instance_type = input("Enter instance_type : ")
        key_pair = input("Enter key-pair name : ")
        security_group = input("Enter security_group name : ")
        subnet_id = input("Enter subnet_id : ")
        os.system("aws ec2 run-instances --image-id {} --key-name {} --security-group-ids {} --subnet-id {} --count 1".format(image_id,key_pair,security_group,subnet_id))

    elif x == 5: # to create s3 bucket
        bucket_name = input("Enter Bucket_name : ")
        control_list = input("Enter Access control list : ")
        region_name = input("Enter region where bucket should deployed : ")
        os.system("aws s3pi create-bucket --bucket {} --acl {} --create-bucket-configuration LocationConstraint={}".format(bucket_name,control_list,region_name))

    elif x == 6: #to delete s3 bucket
        a = input("Enter the name of the bucket to be deleted : ")
        os.system("aws s3pi delete-bucket --bucket {}".format(a))
        print("Deleteed ...")


    elif x == 7: #to delete key-pair
        a = input("Enter the name of the key-pair u want to delete")
        os.system("aws ec2 delete-key-pair --key-pair {}".format(a))
        print("{a} deleted")

    elif x == 8: #launch an instance with configured web server
        q = input ("Enter Image id : ")
        w = input ("Specify Instance type : ")
        a = input ("Specify Key-pair : ")
        e = input ("Enter Security Group id : ")
        r = input ("Enter subnet-id : ")
         os.system ("aws ec2 run-instances  --image-id  {}  --instance-type {} --key-name {}  --security-group-ids {} --subnet-id {} --count 1   ".format(q,w,a,e,r))


        #Configuring webpage

        ip = input ("Enter  ip of the instance : " )
        print("\t\t\tNOTE \nCheck the key downloaded and the program is in the same folder.")
        key = input ("Enter key-name without any extension :")
        os.system("ssh -l ec2-user {} -i {}.pem sudo yum install httpd  ".format(ip,key))
        webpage = input ("Enter the path where the web page is located : ")
        os.system("ssh -l ec2-user {} -i {}.pem sudo cp {} /var/www/html/".format(ip.key,webpage))
        os.system("ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))


    elif x == 9: #to start an instance
        instance_id = input("Enter Instance ids : ")
        os.system("aws ec2 start-instances --instance-ids {}".format(instance_id))
        print()


    elif x == 10: # to stop an instance
        instance_id = input("Enter instance id : ")
        os.system("aws ec2 stop-instances --instance-ids {}".format(instance_id))
        print()


    elif x == 11: #to terminate an instances
        instance_id = input("Enter instance id : ")
        os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))
        print()

    elif x == 12: # to create a cloudfront distribution
        origin = input("Enter origin domain name :")
        object1 = input ("Enter object name : ")
        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.aws.com --default-root-object {}".format(origin,object1))

     elif x == 13: # to attach volume
        q = input ("Provide with a device name of the Volume to be attached (for ex: /dev/sdh) : ")
        w = input ("Provide with a instance id to which you want to connect the volume with : ")
        e = input ("Specify the Volume id : ")
        os.system("aws ec2 attach-volume  --device {} --instance-id {} --volume-id {} ".format(q,w,e))
        print()

    elif x == 14:
        os.system("exit")
        break

    else:
        print(colored("Invalid Input !!!!!","red"))

                                                                        22,54         Top

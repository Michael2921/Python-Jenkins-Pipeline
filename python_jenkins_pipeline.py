import boto3
import os
import paramiko
import subprocess


ecr_client = boto3.client('ecr', region_name="us-east-1")

repositories = ecr_client.describe_repositories()



tag_list = ecr_client.describe_images(repositoryName="python-app")

tag_choices = []



def get_images():

    for tag in tag_list['imageDetails']:
        try:
            tag_choices.append(tag['imageTags'][0])

        except KeyError:
            continue

    return tag_choices


def ssh_access():

     public_ipv4 = '100.53.51.251'

     ssh = paramiko.SSHClient()

     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

     ssh.connect(public_ipv4, username='ec2-user', key_filename='/var/jenkins_home/.ssh/id_rsa')


     return ssh


image_choice = os.getenv("CHOICE_ENV")

#access_key_id = os.getenv("AWS_ACCESS_KEY_ID") test to see if the defined variable in jenkins will work here
#secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
repo_name  = "420392929933.dkr.ecr.us-east-1.amazonaws.com/python-app"

def deploy_image(image):

    ssh = ssh_access()

    ecr_login = subprocess.run(
       "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 420392929933.dkr.ecr.us-east-1.amazonaws.com",
        shell=True,
        capture_output=True,
        text=True
    )

    print(ecr_login.stdout)
    print(ecr_login.stderr)

    run_command_1 = subprocess.run(
        ["docker", "run", "-p" "8080:80" "-d" f"{repo_name}:{image}"], # subprocess.run() waits for the command to finish running
        capture_output=True,
        text=True
    )

    print(run_command_1.stdout)
    print(run_command_1.stderr)

    run_command_2 = subprocess.run(
        ["docker", "run", "-p" "8080:8080" "-d" f"{repo_name}:{image}"],
        # subprocess.run() waits for the command to finish running
        capture_output=True,
        text=True
    )

    print(run_command_2.stdout)
    print(run_command_2.stderr)

    run_command_3 = subprocess.run(
        ["docker", "run", "-p" "8080:8080" "-d" f"{repo_name}:{image}"],
        # subprocess.run() waits for the command to finish running
        capture_output=True,
        text=True
    )

    command_list = {1.0:[run_command_1]}, {2.0:[run_command_2]}, {3.0:[run_command_3]}

    for key, value in command_list.items():
        if key == image_choice:
            print(f"{key} is {value}")
            value

    print(run_command_3.stdout)
    print(run_command_3.stderr)


    ssh.close()

get_images()
for choice in tag_choices:
    if image_choice == choice:
        deploy_image(choice)






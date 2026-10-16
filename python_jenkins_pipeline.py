import boto3
import os
import paramiko
from functools import partial


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

access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
repo_name  = "420392929933.dkr.ecr.us-east-1.amazonaws.com/python-app"

def deploy_image(image):

    ssh = ssh_access()

    try:


        remote_command = (
            f"export AWS_ACCESS_KEY_ID={access_key_id} && export AWS_SECRET_ACCESS_KEY={secret_access_key} && "
            f"aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 420392929933.dkr.ecr.us-east-1.amazonaws.com"
        )


        stdin, stdout, stderr = ssh.exec_command(remote_command)

        exit_code = stdout.channel.recv_exit_status()

        print(stdout.read().decode())
        print(stderr.read().decode())

        if exit_code != 0:
            raise RuntimeError("ECR login failed")



        run_command_2 = partial(
            ssh.exec_command,
            f"docker run -p 8080:8080 -d {repo_name}:{image}"
        )




        run_command_1 = partial(
            ssh.exec_command,
            f"docker run -p 8080:80 -d {repo_name}:{image}"

        )


        run_command_3 = partial(
            ssh.exec_command,
            f"docker run -p 8080:8080 -d {repo_name}:{image}"

        )



        command_list = {"1.0":[run_command_1], "2.0":[run_command_2], "3.0":[run_command_3]}

        for tag, commands in command_list.items():
            for command in commands:
                if image_choice == tag:
                    stdin, stdout, stderr =  command()
                    exit_code = stdout.channel.recv_exit_status()
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                    if exit_code != 0:
                        print("Docker container failed to start")
                    else:
                        print("Docker container started")



    finally:
        ssh.close()

get_images()
for choice in tag_choices:
    if image_choice == choice:
        deploy_image(choice)






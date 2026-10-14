#!/usr/bin/env groovy


pipeline {
    agent any

    environment {
        ECR_REPO_SERVER = '420392929933.dkr.ecr.us-east-1.amazonaws.com/python-app'

    }

    stages {



        stage('Select ECR image') {

            steps{
                script {
                def output = sh(script: "python3 -c 'import python-jenkins-pipeline; print(\"\\n\".join(python-jenkins-pipeline.get_images()))'", // .join converts python list to a string with a newline between each string
                returnStdout: true
                ).trim()


                def imageChoices = output.readLines() // converts string to list


                echo 'Selecting ECR image'
                env.CHOICE_ENV = input(
                    message: 'Select image to deploy',
                    ok: 'Confirm',
                    parameters: [
                        choice(name: 'Images', choices: imageChoices, description: 'What to deploy?')
                    ]
                )


                }
            }


        }




//        stage('Deploying image to EC2 instance') {
//            environment {
//                AWS_ACCESS_KEY_ID = credentials('jenkins_aws_access_key_id')
//                AWS_SECRET_ACCESS_KEY = credentials('jenkins_aws_secret_access_key')
//            }
//            steps {
//                script {
//                        echo 'Deploying the application to EC2'
//                        sh "python3 ./python-jenkins-pipeline.py"
//                }
//            }
//        }
    }
}


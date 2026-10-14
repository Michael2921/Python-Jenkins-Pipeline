#!/usr/bin/env groovy


pipeline {
    agent any

    environment {
        ECR_REPO_SERVER = '420392929933.dkr.ecr.us-east-1.amazonaws.com/python-app'

    }

    stages {



//        stage('Select ECR image') {
//
//            steps{
//                script {
//                echo 'Selecting ECR image'
//                def doStuff = input(
//                    message: 'Select target environment',
//                    ok: 'Confirm',
//                    parameters: [
//                        choice(name: 'ENV', choices: ['Dev', 'Staging', 'Prod'], description: 'Where to deploy?')
//                    ]
//                )
//
//                echo "The chosen environment is: ${doStuff}"
//
//                }
//            }
//
//
//        }



        stage('Select ECR image') {

            steps{
                script {
                echo 'Selecting ECR image'
                def doStuff = input(
                    message: 'Enter your custom value',
                    ok: 'Confirm',
                    parameters: [
                        string(name: 'USER_INPUT', defaultValue '', description: 'Please type the value you want to use:')
                    ]
                )

                echo "The chosen environment is: ${doStuff}"

                }
            }


        }



        stage('Deploying image to EC2 instance') {
            steps {
                script {
                        echo 'Deploying the application to EC2'
                }
            }
        }
    }
}
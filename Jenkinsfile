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
                echo 'Selecting ECR image'

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
pipeline {
    agent any

    stages {
        // Stage 1: Download your latest code from GitHub
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Stop the old containers and clean up
        stage('Tear Down Old System') {
            steps {
                sh 'docker-compose down'
            }
        }

        // Stage 3: Build the new images and turn everything on in the background
        stage('Build & Deploy New System') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
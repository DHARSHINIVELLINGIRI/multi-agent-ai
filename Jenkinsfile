pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = "your_dockerhub_username"
    }
    stages {
        stage('Stage 1: Clone') {
            steps { checkout scm }
        }
        stage('Stage 2: Build') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Stage 3: Docker Create & Push') {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/multi-agent-ai:latest ."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo \$PASS | docker login -u \$USER --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/multi-agent-ai:latest"
                }
            }
        }
    }
}
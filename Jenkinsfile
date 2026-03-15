pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'patoqueipo'
        DOCKERHUB_PASS = credentials('dockerhub-password')
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Patuski/proyecto-ci-cd-Patuski.git'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest test_app.py'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/flask-app:latest .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
                sh 'docker push $DOCKERHUB_USER/flask-app:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}

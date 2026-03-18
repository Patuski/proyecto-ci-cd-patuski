pipeline {
    agent any

    environment {
        // Asegúrate de que este ID sea el que creaste en Jenkins para DockerHub
        DOCKER_CREDS = credentials('dockerhub-id') 
        DOCKER_USER = 'patoqueipo'
    }

    stages {
        stage('Clone') {
            steps {
                // No necesitamos 'git ...' aquí porque Jenkins ya lo clonó.
                // Ponemos un mensaje para que la etapa aparezca en el Stage View.
                echo 'Código descargado correctamente desde GitHub.'
            }
        }

        stage('Test') { 
            steps {
                // Instalación y ejecución de pruebas [cite: 12, 39]
                sh 'pip3 install flask pytest --break-system-packages'
                sh 'python3 -m pytest test_app.py'
            }
        }

        stage('Build Image') { 
            steps {
                // Construcción de la imagen [cite: 14, 40]
                sh "docker build -t ${DOCKER_USER}/flask-app:latest ."
            }
        }

        stage('Push to DockerHub') { 
            steps {
                // Subida a DockerHub [cite: 15, 41]
                sh "echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin"
                sh "docker push ${DOCKER_USER}/flask-app:latest"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps {
                // Despliegue final [cite: 16, 42, 43, 44]
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}

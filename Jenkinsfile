pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Récupération du code GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-student-portal:v2 .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop portail-etudiants || true
                docker rm portail-etudiants || true
                docker run -d -p 5000:5000 --name portail-etudiants devops-student-portal:v2
                '''
            }
        }
    }
}

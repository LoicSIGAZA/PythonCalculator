pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t python-calculator .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                bat 'docker run --rm python-calculator'
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                echo 'Running tests inside container...'
                bat 'docker run --rm python-calculator python -m unittest discover'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

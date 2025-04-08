pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'No external dependencies to install.'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat 'python -m unittest discover'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jenkins-devops-app .'
            }
        }

        stage('Pipeline Complete') {
            steps {
                echo 'CI/CD pipeline completed successfully!'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All stages passed.'
        }
        failure {
            echo 'FAILED: Check the Console Output.'
        }
    }
}
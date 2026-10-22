pipeline {
    agent any

    environment {
        PYTHON = 'C:/Users/Akhil.Pradeep/AppData/Local/Programs/Python/Python39/python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
    steps {
        bat '"C:\\Users\\Akhil.Pradeep\\AppData\\Local\\Programs\\Docker\\Docker\\resources\\bin\\docker.exe" --version'
        bat '"C:\\Users\\Akhil.Pradeep\\AppData\\Local\\Programs\\Docker\\Docker\\resources\\bin\\docker.exe" build -t jenkins-devops-app .'
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

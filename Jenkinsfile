pipeline {
agent any


environment {
    PYTHON = 'C:/Users/Akhil.Pradeep/AppData/Local/Programs/Python/Python312/python.exe'
    DOCKER = 'C:\\Users\\Akhil.Pradeep\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    IMAGE_NAME = 'jenkins-devops-app'
}

stages {
    stage('Checkout') {
        steps {
            echo 'Source code is retrieved from GitHub by Jenkins SCM.'
        }
    }

    stage('Check Python and Docker') {
        steps {
            bat '"%PYTHON%" --version'
            bat '"%PYTHON%" -m pip --version'
            bat '"%DOCKER%" --version'
        }
    }

    stage('Install Dependencies') {
        steps {
            bat '"%PYTHON%" -m pip install -r requirements.txt'
        }
    }

    stage('Code Quality Check') {
        steps {
            bat '"%PYTHON%" -m ruff check app.py test_app.py'
        }
    }

    stage('Run Tests with Coverage') {
        steps {
            bat '"%PYTHON%" -m pytest --cov=app --cov-report=term-missing --cov-report=xml:coverage.xml --junitxml=test-results.xml -v'
        }
    }

    stage('Dependency Security Audit') {
        steps {
            bat '"%PYTHON%" -m pip_audit -r requirements.txt'
        }
    }

    stage('Build Docker Image') {
        steps {
            bat '"%DOCKER%" build -t %IMAGE_NAME% .'
        }
    }

    stage('Deploy Docker Container') {
    steps {
        script {
            bat '''
                "%DOCKER%" rm -f jenkins-devops-app 2>NUL
                if errorlevel 1 exit /b 1
                "%DOCKER%" run -d --name jenkins-devops-app -p 5000:5000 --restart unless-stopped %IMAGE_NAME%
                if errorlevel 1 exit /b 1
            '''
        }
    }
}
    groovy
stage('Trivy Security Scan') {
    steps {
        script {
            bat '''
                echo Running Trivy vulnerability scan...
                "C:\\trivy\\trivy.exe" image --scanners vuln --severity HIGH,CRITICAL --exit-code 0 --no-progress %IMAGE_NAME%
            '''
        }
    }
}



    stage('Pipeline Complete') {
        steps {
            echo 'CI pipeline completed successfully!'
        }
    }
}

post {
    always {
        script {
            if (fileExists('test-results.xml')) {
                junit testResults: 'test-results.xml',
                      allowEmptyResults: true
            }

            if (fileExists('coverage.xml')) {
                archiveArtifacts artifacts: 'coverage.xml',
                                 allowEmptyArchive: true
            }
        }
    }

    success {
        echo 'SUCCESS: Quality checks, tests, dependency audit, and Docker build passed.'
    }

    failure {
        echo 'FAILED: Check Console Output to identify the failing stage.'
    }
}


}

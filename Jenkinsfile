pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/TomKuc/ium_s444420.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                pip install sacred datasets scikit-learn joblib
                '''
            }
        }

        stage('Run experiment') {
            steps {
                sh '''
                python3 train.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'sacred_runs/**/*', fingerprint: true
        }
    }
}

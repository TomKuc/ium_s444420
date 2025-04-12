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
                python3 imu_07/imu_07.py
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

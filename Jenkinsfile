pipeline {
    agent any

    stages {
        stage('Checkout Repository') {
            steps {
                git branch: 's444420-create-dataset-docker', url: 'https://github.com/TomKuc/ium_s444420.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t dataset-processor .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run --rm -v $(pwd):/app dataset-processor'
                }
            }
        }

        stage('Archive Processed Data') {
            steps {
                archiveArtifacts artifacts: 'final_data.csv', fingerprint: true
            }
        }
    }
}

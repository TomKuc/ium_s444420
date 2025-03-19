pipeline {
    agent any

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }

        stage('Copy Dataset Artifact') {
            steps {
                copyArtifacts(
                    fingerprintArtifacts: true, 
                    projectName: 'z-s444420-create-dataset', 
                    selector: lastSuccessful()
                )
            }
        }

        stage('Pull Docker Image') {
            steps {
                script {
                    sh 'docker pull ubuntu:latest'
                }
            }
        }

        stage('Run Statistics Script in Container') {
            steps {
                script {
                    sh 'docker run --rm -v $(pwd):/app -w /app ubuntu:latest bash stats_script.sh final_data.csv'
                }
            }
        }

        stage('Archive Statistics') {
            steps {
                archiveArtifacts artifacts: 'stats_result.txt', fingerprint: true
            }
        }
    }
}
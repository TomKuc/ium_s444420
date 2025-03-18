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

        stage('Run Statistics Script') {
            steps {
                sh "bash stats_script.sh final_data.csv"
            }
        }

        stage('Archive Statistics') {
            steps {
                archiveArtifacts artifacts: 'stats_result.txt', fingerprint: true
            }
        }
    }
}

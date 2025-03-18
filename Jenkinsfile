pipeline {
    agent any

    parameters {
        string(name: 'BUILD_SELECTOR', defaultValue: 'lastSuccessful', description: 'Wybierz build do skopiowania artefaktów')
    }

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
                    selector: buildParameter('BUILD_SELECTOR')
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
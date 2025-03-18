pipeline {
    agent any

    parameters {
        string(name: 'CUTOFF', defaultValue: '3', description: 'Liczba pierwszych/losowych przykładów do wybrania')
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }

        stage('Run Shell Script') {
            steps {
                sh "bash process_data.sh ${params.CUTOFF}"
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'final_data.csv', fingerprint: true
            }
        }
    }
}
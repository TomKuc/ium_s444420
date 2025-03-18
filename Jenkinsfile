pipeline {
    agent any 
    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Shell Script') {
            steps {
                sh './process_data.sh'
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'final_data.csv', fingerprint: true
            }
        }
    }
}

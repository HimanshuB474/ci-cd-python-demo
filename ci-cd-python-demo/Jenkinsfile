pipeline {
    agent any

    environment {
        ARTIFACTORY_CREDS = credentials('artifactory-credentials')
        PYTHON = 'python3'
        PIP = 'pip3'
    }

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    extensions: [[$class: 'CleanBeforeCheckout']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/HimanshuB474/ci-cd-python-demo.git',
                        credentialsId: 'github-credentials'
                    ]]
                ])
                sh 'git branch -a'
                sh 'ls -la' // List files to verify checkout
            }
        }

        stage('Build with Maven') {
            steps {
                script {
                    sh 'echo "Checking files in Jenkins workspace..."'
                    sh 'ls -la'  // Confirm pom.xml is present
                    sh 'mvn clean install'  // Run Maven directly
                }
            }
        }

        // You can add testing, deployment stages here if needed
    }

    post {
        always {
            cleanWs()
        }
        success {
            slackSend(color: 'good', message: "SUCCESS: ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
        failure {
            slackSend(color: 'danger', message: "FAILED: ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
            emailext body: '''
                Check console output at ${BUILD_URL}
                
                Failed stage: ${STAGE_NAME}
                Error: ${BUILD_LOG_REGEX, regex="ERROR:.*", linesBefore=5, linesAfter=5}
            ''',
            subject: 'FAILED: ${JOB_NAME} #${BUILD_NUMBER}',
            to: 'dev-team@example.com'
        }
    }
}

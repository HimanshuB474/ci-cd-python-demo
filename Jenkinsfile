pipeline {
    agent any

    environment {
        PYTHON = 'python'
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
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/HimanshuB474/ci-cd-python-demo.git',
                        credentialsId: 'github-credentials'
                    ]]
                ])
                bat 'dir' // Windows uses 'dir', not 'ls -la'
            }
        }

        stage('Build and Test') {
            steps {
                bat 'mvn clean install'
            }
        }
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
            emailext(
                body: '''Check console output at ${BUILD_URL}
                
                Failed stage: ${STAGE_NAME}
                Error: ${BUILD_LOG_REGEX, regex="ERROR:.*", linesBefore=5, linesAfter=5}''',
                subject: 'FAILED: ${JOB_NAME} #${BUILD_NUMBER}',
                to: 'dev-team@example.com'
            )
        }
    }
}
